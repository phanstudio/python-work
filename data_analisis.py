from numpy.core.fromnumeric import size
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import csv
#from sqlalchemy import create_engine
from urllib import request
#import html5lib

x = np.genfromtxt("npr.txt", "int8", delimiter= ",")
x = np.resize(x, 22)
x = x[x>20]
print(x)

if False:
  a = np.random.randint(3, 7, size= (2,5), dtype= "int8")
  b = np.full(a.shape, 9, dtype= a.dtype)
  b = np.full_like(b, 6)
  #b = b + - / ** * cos sin matmul identify linalg.def, min(axis), max(axis), sum(axis), axis depends on shape 0, 1, 2
  #b = a.reshape((5,2)) vstack(a,b,b,b) od arrays(a,b)
  print(a)
  print(b)
if False:
    html_string = """
    <table>
        <thead>
          <tr>
            <th>Order date</th>
            <th>Region</th> 
            <th>Item</th>
            <th>Units</th>
            <th>Unit cost</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1/6/2018</td>
            <td>East</td> 
            <td>Pencil</td>
            <td>95</td>
            <td>1.99</td>
          </tr>
          <tr>
            <td>1/23/2018</td>
            <td>Central</td> 
            <td>Binder</td>
            <td>50</td>
            <td>19.99</td>
          </tr>
          <tr>
            <td>2/9/2018</td>
            <td>Central</td> 
            <td>Pencil</td>
            <td>36</td>
            <td>4.99</td>
          </tr>
          <tr>
            <td>3/15/2018</td>
            <td>West</td> 
            <td>Pen</td>
            <td>27</td>
            <td>19.99</td>
          </tr>
        </tbody>
    </table>
    """
    """d = np.arange(5, dtype= "int8")
    print(d.dtype)"""
    """data = request.urlopen("https://my-vampire-system.fandom.com/wiki/Quinn_Talen")
    response = data.read()"""
    with open("vsm.html", "rb") as f:
        response = f.read()
    dat = pd.read_html("https://my-vampire-system.fandom.com/wiki/Quinn_Talen", flavor="html5lib")
    print(dat)

    """engine = create_engine("sqlite:///chinook.db")
    connection = engine.connect()
    db = pd.read_sql_table("employees", con=connection)
    print(db.head())
    #read_sql_table(), read_sql_quere(), read_sql"""
if False:
    """data = pd.read_csv("enrollment.csv")
    dat = data["status"] #"canceled"
    dat2 = data["account_key"]
    plt.plot(dat2, dat, "o")
    plt.show()"""

    """a = np.array([1, 2, 3, 4])
    b = np.array([0, 0.5, 1, 1.5, 2])
    c = np.array([1, 2, 3, 4, 9], np.int8)
    d = np.random.random((3,2))
    e = d[:, 0] = 9
    f = d.sum()
    g = d.std()
    h = d.mean(axis= 0)
    i = np.arange(5)
    j = i + 20
    k = j * 5
    l = j + k
    m = np.arange(4)
    #i[[True,False,True,False,True]]
    #i[(i%2==0) & (i>i.mean())]"""

    """li = [i for i in range(20) if i % 2 == 0 and i % 3 == 0]
    ly = pd.Series(li)
    ly.name = "poper"
    ly.index =[
        "lo",
        "po",
        "li",
        "ly",
    ]"""
    """li = [i for i in range(20) if i % 2 == 0 and i % 3 == 0]
    lu = ["log","polg","line","love",]
    dic = {i:li[j] for j, i in enumerate(lu)}
    ly = pd.Series(dic, name= "people")"""
    """li = [i for i in range(20) if i % 2 == 0 and i % 3 == 0]
    lu = ["log","polg","line","love",]
    ly = pd.Series(li, index= lu, name= "people")
    #ly * 1_000
    #ly[ly <= 8]
    #ly[["love", "polg"]]
    ly["kopper"] = 40
    ly[ly < 8] = 0

    li = [i for i in range(20) if i % 2 == 0 and i % 3 == 0]
    ly = [i for i in range(4)]
    lo = [i * sum(li) for i in range(4)]
    bi = [li, ly, lo, li, ly]
    nam = ["niger", "nigeria", "china", "usa", "uk"]
    dic = {i:bi[j] for j, i in enumerate(nam)}
    kop = pd.DataFrame(dic, dtype= np.int8)

    kop["un"] = [1,2,3,4]
    kop.loc[kop["uk"] < 3, "uk"] = 1
    print(kop)"""
if False:
    #kop.size
    #kop.shape
    #kop.info()
    #kop.describe()
    #kop.dtypes
    # kop.sum(), kop.min(), kop.max(), kop.mean(), ko.quantile(), kop.std()
    #kop.loc["1"], kop.loc[0: 2], kop.loc[0: 2, ["niger", "china"]], kop.loc[0: 2, "niger": "china"]
    #kop.iloc[-1], kop.loc[kop["niger"] > 2, ["niger", "nigeria"]]
    #kop.drop(columns=["nigeria"]), kop.drop(0)
    crop = pd.Series([-1_000, -0.3], index= ["niger", "china"])
    print(kop)
    kop[["niger", "china"]] = kop[["niger", "china"]] - crop
    kop.rename(columns={
        "uk": "unitedkingdom",
        },
                index={
        2: "kill count",
        }
    )
    kop["niger per china"] = kop["niger"] / kop["china"]
    print(kop)
if False:
    """data = pd.read_csv("goog.csv")
    data = data[["b'Date","Open"]]
    data.columns = ["date", "price"]
    data["date"] = pd.to_datetime(data["date"])
    data.set_index("date", inplace= True)
    print(data.loc["2020-09-28"])
    print(data.head())"""

    """data = pd.read_csv("goog.csv", index_col=0, parse_dates= True)
    data = data[["Open", "High"]]
    data.columns = ["price", "up"]
    data.loc["2020-09-09":"2020-11-03"].plot()
    plt.show()"""
    """#data = pd.Series([1, np.nan, 0, np.nan])
    li = [(i* 8)+1 for i in range(4)]
    data = pd.DataFrame([["m", "d", "f", "f", "m"],["f", 1, 5, np.nan, 8],li,["f",7,8], ["d"]], columns=["A", "B", "C", "D", "E"])
    #data.isnull().any() #all
    #data.dropna()axis= 1, how= "all", how= "any", thresh = 3
    data.fillna(0)# fillna(data.mean()) method= "ffill", method= "bfill", axis= 1
    data["A"].unique()
    data["A"].value_counts()
    data["A"].replace(1, "m")
    data["A"].replace({1:"m", "d":"f"})
    data = data.replace({"A":{1:"m", "d":"f"}, "B":{None: 30, "d": 70}})
    data.loc[data["B"] < 20, "B"] = data.loc[data["B"] < 20, "B"] + 20
    print(data)"""
if False:
    li = ["A","B","C","D","F","G","H"]
    ly = [2,3,3,7,7,8,7]
    lu = ["r","t","r","g","u","t","r"]

    """numb = pd.Series(ly, index= li, name= "population")
    numb.duplicated(keep= "last")
    numb.drop_duplicates()
    numb = pd.DataFrame(index=li, data= {"pup":lu,"lop":ly})
    numb.duplicated(subset="pup")

    numb = pd.DataFrame({
        "pup":[
            "1987_M_US _1",
            "1990?_M_Uk_1",
            "1992_F_US_2",
            "1970?_M_   IT_1",
            "1985_F_I T_2",
        ],
        })

    numb = numb["pup"].str.split("_", expand=True)
    numb.columns = ["Date", "Gender", "Country", "No_children"]
    #(numb["Date"].str.contains("\?"))#\? if the last letter is "?"
    #numb["Country"].str.contains("U")
    numb["Country"] = numb["Country"].str.strip()
    numb["Country"]  = numb["Country"].str.replace(" ", "")
    numb["Date"] = numb["Date"].str.replace(r"(?P<date>\d{4})\?", lambda m: m.group("date"))
    """

"""with open("goog.csv", "r") as f:
    data = csv.reader(f)
    for index, values in enumerate(data):
        u,i,o,p,l,j,k = values
        if (index - 1) < 10 and index != 0:
            print(f"{index - 1}  {u}  ${i} {o}")
        if index == 0:
            print(f"   {u}      ${i}        {o}")

#pd.read_html()
data = pd.read_csv("goog.csv")
data = data[["b'Date", "Open", "High"]]
print(data.head(10))
#data.to_csv()"""
