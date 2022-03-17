"""
if True:
    from sklearn import linear_model, model_selection
    import numpy as np
    import pickle
    import pandas as pd

    csv = "student-mat.csv"
    data = pd.read_csv(csv, sep= ";")
    data = data[["age","Medu","Fedu","traveltime","studytime","failures","famrel","freetime","goout","Dalc","Walc","health","absences","G1","G2","G3"]]
    #age;Medu;Fedu;traveltime;studytime;failures;famrel;freetime;goout;Dalc;Walc;health;absences;G1;G2;G3
    predict = "G3"

    x = np.array(data.drop([predict], 1))
    y = np.array(data[predict])

    number_of_test = 30
    test_acc = 0.1
    train = False

    x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size= test_acc)

    if train == True:
        best = 0
        for _ in range(number_of_test):
            x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size= test_acc)
            linear = linear_model.LinearRegression()
            linear.fit(x_train, y_train)
            acc = linear.score(x_test, y_test)
            print(acc)
            if acc > best:
                best = acc
                with open("model_accuracy", "w") as fa:
                    fa.write(str(best))
                with open("student_model2.pickle", "wb") as f:
                    pickle.dump(linear, f)
    else:
        f = open("student_model2.pickle", "rb")
        linear = pickle.load(f)

        fa = open("model_accuracy", "r")
        best = fa.read()
        print("Prediction accuracy: ", best)
        predictions = linear.predict(x_test)

        for x in range(len(predictions)):
            print("Prediction: ", predictions[x], " Values: ", x_test[x], " Predict: ", y_test[x])
"""

if True:
    from scipy.sparse import data
    from sklearn import model_selection
    from sklearn.utils import shuffle
    from sklearn.neighbors import KNeighborsClassifier
    import pandas as pd
    import numpy as np
    from sklearn import linear_model, preprocessing

    data = pd.read_csv("car.data")

    le = preprocessing.LabelEncoder()
    buying = le.fit_transform(list(data["buying"]))
    maint = le.fit_transform(list(data["maint"]))
    door = le.fit_transform(list(data["door"]))
    persons = le.fit_transform(list(data["persons"]))
    lug_boot = le.fit_transform(list(data["lug_boot"]))
    safety = le.fit_transform(list(data["safety"]))
    cls = le.fit_transform(list(data["class"]))

    predict = "class"

    x = list(zip(buying, maint, door, persons, lug_boot, safety))
    y = list(cls)

    x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size= 0.1)

    model = KNeighborsClassifier(n_neighbors=7)

    model.fit(x_train, y_train)
    acc = model.score(x_test, y_test)
    print(acc)

    prediction = model.predict(x_test)
    names = ["unacc", "acc", "good", "vgood"]

    for x in range(len(prediction)):
        print("Prediction: ", names[prediction[x]], "Data: ", x_test[x], "Actual: ", names[y_test[x]])
        #n = model.kneighbors([x_test[x]], 7, True)
        #print(n)

