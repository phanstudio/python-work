from matplotlib import pyplot as plt
#from matplotlib import image as mpimg
import numpy as np
#import pandas as pd
import random as rd
#from PIL import Image
import time

def O(fn):
    def wrapper(*args):
        n = 0
        start_time = time.time()
        #Here you add code
        n = fn(*args)
        final_time = time.time()
        timer = final_time - start_time
        timer = round(timer, 8)
        #print(timer, "sec")
        return timer, n
    return wrapper

def create(lis: list, num = 0):
    li = []
    for i in lis:
        x = []
        for _ in range(i):
            x.append(rd.randint(0, 10))
        li.append(x)
    if num != 0:
        return li[:num]
    else:
        return li

@O
def add_li(li: list):
    total = 0
    for i in li:
        total += i
    return len(li)

li = [1,8,9,6,7,10,12,20,39,10000, 100000]
for i in range(1, 20):
    if i not in li:
        li.append(i)
li.sort()
lix = list(create(li))
liz = []
liy = []
for i in lix:
    liz.append(add_li(i)[0])
    liy.append(add_li(i)[1])

plt.plot(liy, liz, marker= "o")
plt.xlim(0)
plt.ylim(0)
plt.show()

"""
np.zeros((10, 2,4), dtype= np.int)
np.ones((9,8,7))
np.arange(20)
np.eye(5,6,1)
np.random.randn(50)
np.random.random((2,4,6,1))

np.full((2, 2), 9)
np.array([9,9,4,6], dtype= "int8")
np.linspace(6, 8, 10)
z = np.full((2, 3), 3)
b = np.full((2,3,2),4)
n = np.full_like(b, 100)

np.sum(b)
#z+b z*b z/b z-b np.dot(z,b) b.T
n = np.sum(b, axis= 2)
x = n
print(x)
"""
"""img = Image.open(r"asset\opp.jpg")
img.thumbnail((64, 64), Image.ANTIALIAS)
imgplot = plt.imshow(img, interpolation= "nearest")
#imgplot = plt.imshow(img, interpolation= "bicubic")
plt.show()"""

"""img = mpimg.imread(r"asset\opp.jpg")
lum_img = img[:, :, 0]
fig = plt.figure()
ax = fig.add_subplot(1, 2, 1)
imgplot = plt.imshow(lum_img)
ax.set_title("Before")
plt.colorbar(ticks= [50, 100, 150, 200, 250], orientation= "horizontal")

ax = fig.add_subplot(1, 2, 2)
imgplot = plt.imshow(lum_img)
imgplot.set_clim(50, 250)
ax.set_title("After")
plt.colorbar(ticks= [50, 100, 150, 200, 250], orientation= "horizontal")
plt.show()"""

"""img = mpimg.imread(r"asset\opp.jpg")
lum_img = img[:, :, 0]
imgplot = plt.imshow(lum_img)
#imgplot = plt.imshow(lum_img, clim= (0.0, 200.0))
plt.colorbar()
#plt.hist(lum_img.ravel(), bins= 256, range= (0.0, 1.0), fc= "k", ec= "k")
#imgplot.set_cmap("nipy_spectral")
#imgplot = plt.imshow(lum_img, cmap="hot")
plt.show()
#print(img)"""

"""data = {"Barton LLC": 109438.50,
        "Frami, Hills and Schmidt": 103569.59,
        "Fritsch, Russel and Anderson": 112214.71,
        "Jerde-Hilpert": 112591.43,
        "Keeling LLC": 100934.30,
        "Koepp Ltd": 103660.54,
        "Kulas Inc": 137351.96,
        "Trantow-Barrows": 123381.38,
        "White-Trantow": 135841.99,
        "Will LLC": 104437.60}

group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)

def currency(x, pos):
    if x >= 1e6:
        s = "${:1.1f}M".format(x*1e-6)
    else:
        s = "${:1.1f}K".format(x*1e-3)
    return s
plt.style.use("fivethirtyeight")
#plt.style.use("dark_background")
#print(plt.style.available)
plt.rcParams.update({"figure.autolayout": True})

fig, ax = plt.subplots(figsize= (9, 4))
ax.barh(group_names, group_data)
lables = ax.get_xticklabels()
plt.setp(lables, "rotation", 45, "horizontalalignment", "right")

ax.axvline(group_mean, ls= "--", color= "r", lw= 2)
for group in [3, 5, 8]:
    ax.text(145000, group, "New Company", fontsize= 10,
            verticalalignment= "center")

ax.title.set(y= 1.05)
ax.set(xlim= [-1000, 140000], xlabel= "Total Revenue", ylabel= "Company", title= "Company Revenue")
ax.xaxis.set_major_formatter(currency)
ax.set_xticks([0, 25e3, 50e3, 75e3, 100e3, 125e3])
fig.subplots_adjust(right= 0.1)

plt.show()"""

"""ax = plt.subplot()
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)

line, = plt.plot(t, s, lw= 1)
plt.annotate("local max", xy= (2, 1), xytext= (3, 1.5),
            arrowprops= dict(facecolor = "black", shrink= 0.05),
    )

plt.ylim(-2, 2)
plt.xlim(left= 0)
plt.show()"""

"""mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
n, bins, patches = plt.hist(x, 50, density= 1, facecolor= "g", alpha= 0.75)

plt.xlabel("Smarts")
plt.ylabel("Probability")
plt.title("Histogram of IQ")
plt.text(60, 0.025, r"$\mu=100,\ \sigma= 15$", color= "red", fontsize= 10)
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()"""

#plt.title(r"$\sigma_i= 15$")
#plt.show()

"""plt.figure(1)
plt.subplot(211)
plt.plot([1,2,3,4,5,6])
plt.subplot(212)
plt.plot([1,3,3,4,4,6])
plt.clf()

plt.figure(2)
plt.plot([6,3,4,4,3,6])
plt.close()

plt.figure(1)
plt.subplot(211)
plt.plot([1,2,3,3,2,1])
plt.cla()

plt.show()"""
"""
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), "bo", t2, f(t2), "k")
plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), "r--")
plt.show()
"""

"""t1 = np.arange(0.0, 5.0, 0.1)
t = np.exp(t1) * np.cos(2*np.pi*t1)
print(t)"""

"""
x = []
y = []
for i in range(100):
    x.append(rd.randint(-40, 40))
    y.append(rd.randint(-40, 40))

x1 = [1, 2, 3]
y1 = np.array([[1, 2], [3, 4], [5, 6]])
plt.plot(x1, y1)
plt.show()
"""

"""line = plt.plot(x, marker= "o")
plt.setp(line, "color", "r", "linewidth", 1.0, "markersize", 2)
plt.show()"""

"""names = ["Group A", "Group B", "Group C"]
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(121)
plt.bar(names, values)
plt.subplot(122)
plt.scatter(names, values)
plt.suptitle("Categorical Plotting")
plt.show()"""

"""
names = ["Group A", "Group B", "Group C"]
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values, marker= "o")
plt.suptitle("Categorical Plotting")
plt.show()
"""

"""
data = {"a" : np.arange(50),
        "c" : np.random.randint(0,50,50), #color of each circle
        "d" : np.random.randn(50) #scale of each circle
    }
data["b"] = data["a"] + 10 * np.random.randn(50)
data["d"] = np.abs(data["d"]) * 100

plt.scatter("a", "b", c= "c", s= "d", data= data) #a b are the points of each circle, c is the color of each point, s is the scaleq
plt.xlabel("entry A")
plt.ylabel("entry B")
plt.show()
"""

"""x = np.arange(0., 5., 0.2)

#plt.plot(x, marker= "d")
plt.plot(x, x,"d", x, x**2,"+", x, x*10,"v", x, x*4,"p", x, x*7)
plt.show()"""

"""
x = []
y = []
for i in range(100):
    x.append(rd.randint(-40, 40))
    y.append(rd.randint(-40, 40))

plt.plot(x, y, y, x, marker= "d")
plt.show()
"""

"""
def plotter(d1, d2, p_dict, title = "Coords", colr = "Red", ylable = "Y-section", xlable = "X-section", subpltx = 1, subplty = 1):
    fig, ax = plt.subplots(subpltx, subplty)
    out = ax.plot(d1, d2, marker= p_dict, color = colr)
    ax.grid(True)
    ax.set_title(title)
    limy = True
    limx = True
    for d in d2:
        if d < 0:
            limy = False
    if limy:
        ax.set_ylim(0)
    for d in d1:
        if d < 0:
            limx = False
    if limx:
        ax.set_xlim(0)
    ax.set_ylabel(ylable)
    ax.set_xlabel(xlable)
    plt.show()
    return out

x = [9, 7, 4, 3, 2, 1, 0]
y = [9, 8, 4, 3, 2, 1, 0]

x1 = []
y1 = []
for _ in range(100):
    x1.append(rd.randint(-40, 40))
    y1.append(rd.randint(-40, 40))

plotter(x1, y1, "+")
"""

"""
#fig = plt.figure()
#fig, ax = plt.subplots()
x = [9, 7, 4, 3, 2, 1, 0]
y = [9, 8, 4, 3, 2, 1, 0]
fig, axs = plt.subplots(2,2)

axs[0][0].plot(y, x, marker= "o")#o, x
axs[0][0].grid(True)
axs[0][1].plot(y, y)
axs[0][1].set_ylim(6)
axs[0][1].set_xlim(4)
axs[1][0].plot(x, x)
axs[1][0].set_ylabel("Y-section")
axs[1][0].set_xlabel("X-section")
axs[1][1].plot(x, y)
axs[1][1].set_title("Goat")
plt.show()
"""

"""data = pd.read_csv("pop.csv")
#,caption1,caption2,caption3,

plt.plot(data["caption1"], data["caption2"])
plt.plot(data["caption1"], data["caption2"], "o")
plt.show()
"""
"""
x = [1,2,3,4,5,6,7,8]
y = []
z = []
for i in x:
    if z == []:
        y.append(i**2 + 9 - 10)
        z.append(80 - y[int(len(y) - 1)])
    else:
        y.append(i**3 + 9 - z[int(len(y) - 1)])
        z.append(50 - y[int(len(y) - 1)]) 

plt.plot(x, y)
plt.plot(x, z)
plt.title("Coords")
plt.xlabel("X-coord")
plt.ylabel("(Y and Z) - coord")
plt.legend(["Y-coord", "Z-coord"])
plt.show()
"""
