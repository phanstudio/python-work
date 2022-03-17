import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Sequential, datasets, layers
import numpy as np
import matplotlib.pyplot as plt

data = datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = data.load_data()

class_name = ["T-shirt/top", "Trouser", "Pullover", "Dress","Coat",
                "Sendal", "Shirt", "Sneaker", "Bag", "Ankle_boot"]

train_images = train_images / 255.0
test_images = test_images / 255.0

model = Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128, activation= "relu"),
    keras.layers.Dense(10, activation= "softmax")
])

model.compile(optimizer= "adam", loss= "sparse_categorical_crossentropy", metrics= ["accuracy"])
model.fit(train_images, train_labels, epochs= 5)

test_loss, test_acc = model.evaluate(test_images, test_labels)

#print("Tested Acc: ", test_acc)
#plt.imshow(train_images[7], cmap= plt.cm.binary)
#plt.show()

one = False

if one:
    img = 7
    print(prediction = model.predict([test_images[img]]))
    #prediction = model.predict([test_images[img]])
    """prediction = model.predict([test_images[img]])
    plt.grid(False)
    plt.imshow(test_images[img], cmap= plt.cm.binary)
    plt.xlabel("Actual: " + class_name[test_labels[img]])
    plt.title("Prediction" + class_name[np.argmax(prediction[0])])
    plt.show()"""
else:
    prediction = model.predict(test_images)
    for i in range(10):
        plt.grid(False)
        plt.imshow(test_images[i], cmap= plt.cm.binary)
        plt.xlabel("Actual: " + class_name[test_labels[i]])
        plt.title("Prediction: " + class_name[np.argmax(prediction[i])])
        plt.show()
