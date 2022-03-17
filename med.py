from numpy import NAN, nan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def first():
    data = pd.read_csv("med.csv")
    bmi = (data["height"]/100)**2
    data["overweight"] = data["weight"] / bmi

    data = data[["gluc", "cholesterol", "smoke", "alco", "active","overweight", "cardio"]]
    data.loc[data["gluc"] <= 1, "gluc"] = 0
    data.loc[data["gluc"] >  1, "gluc"] = 1
    data.loc[data["overweight"] <= 25, "overweight"] = 0
    data.loc[data["overweight"] >  25, "overweight"] = 1
    data.loc[data["cholesterol"] <= 1, "cholesterol"] = 0
    data.loc[data["cholesterol"] >  1, "cholesterol"] = 1

    data["overweight"] = data["overweight"].astype("int64")
    data = pd.melt(data, id_vars="cardio", value_vars= ["gluc", "cholesterol", "smoke", "alco", "active","overweight"])
    d = sns.catplot(x= "variable", data= data, kind= "count", hue="value", col= "cardio")
    plt.show()

def second():
    df = pd.read_csv("med.csv")
    df = df[["height", "weight", "ap_hi", "ap_lo"]]
    df.loc[df["ap_lo"] > df["ap_hi"], "ap_lo"] = NAN
    df.loc[df["height"] > df["height"].quantile(0.975), "height"] = NAN
    df.loc[df["height"] < df["height"].quantile(0.025), "height"] = NAN
    df.loc[df["weight"] > df["weight"].quantile(0.975), "weight"] = NAN
    df.loc[df["weight"] < df["weight"].quantile(0.025), "weight"] = NAN
    print(df)

second()