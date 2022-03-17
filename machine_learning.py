from __future__ import absolute_import, division, unicode_literals, print_function
import numpy as np
import pandas as pd
import matplotlib as plt
import tensorflow as tf
import tensorflow.python.feature_column as fc

data_set_train = "https://storage.googleapis.com/tf-datasets/titanic/train.csv"
data_set_eval = "https://storage.googleapis.com/tf-datasets/titanic/eval.csv"

df_train = pd.read_csv(data_set_train)
df_eval = pd.read_csv(data_set_eval)

y_train = df_train.pop("survived")
y_eval = df_eval.pop("survived")

CATEGORICAL_COLUMNS = ["sex", "n_siblings_spouses", "parch", "class", "deck", "embark_town", "alone"]
NUMERICAL_COLUMNS = ["age", "fare"]

feature_columns = []
#print(df_train.head())

for feature_name in CATEGORICAL_COLUMNS:
    vocabulary = df_train[feature_name].unique()
    feature_columns.append(fc.categorical_column_with_vocabulary_list(feature_name, vocabulary))

#print(feature_columns[0])

for feature_name in NUMERICAL_COLUMNS:
    feature_columns.append(fc.numeric_column(feature_name, dtype= tf.float32))

def make_input_fn(data_df, label_df, num_epochs = 10, shuffle = True, batch_size = 32):
    def input_function():
        ds = tf.data.Dataset.from_tensor_slices((dict(data_df) , label_df))
        if shuffle:
            ds = ds.shuffle(1000)
        ds = ds.batch(batch_size).repeat(num_epochs)
        return ds
    return input_function
train_input_fn = make_input_fn(df_train, y_train)
eval_input_fn = make_input_fn(df_eval, y_eval, num_epochs= 1, shuffle= False)

linear_est = tf.estimator.LinearClassifier(feature_columns= feature_columns)
linear_est.train(train_input_fn)
result = linear_est.evaluate(eval_input_fn)

print(result["accuracy"])
result = list(linear_est.predict(eval_input_fn))
for i in range(30):
    print(df_eval.loc[i])
    print(y_eval.loc[i])
    print(result[i]["probabilities"][1])