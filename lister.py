"""
intergers = [1,2,3,4,5,6,7,8,9,0]
floaters = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.0]
item = [1,8,9,7,2,3]
ui, *ux, ji = item
noner = [[8,9], [9,8]]
hi, uk = noner
hi, uk = uk, hi #swapping

print(hi + uk)
print(ui, ux, ji)
print(item)
print(ui,ux,ji)


#the created functions
def expont(x):
    return func3(func2(x)**x, x + 1)

def func2(x):
    return x + x

def func3(x, y):
    return x / y

def is_notequal_to_one(x):
    return x != 1

func4 = lambda x: expont(x) // (x + 1)

#filter and map function
fil = list(filter(is_notequal_to_one, intergers)) 

#filter and map work hand in hand
new_fil = list(map(expont , fil))

sul = list(map(expont,intergers))

new_list = []
for x in floaters:
    if func4(x) != 0:
        new_list.append(func4(x))

li = [expont(x) for x in intergers if x % 2 == 0]

new_li = [expont(x) for x in fil if x % 2 == 0]

#The prints statements
print(sul)
print(new_list)
print(li)
print(fil)
print(new_fil)
print(new_li)

"""

"""
from collections import namedtuple, Counter, deque

g = deque("hello", maxlen= 7)
g.extend("hi")
g.rotate(2)
g.remove("o")
print(g)

c = namedtuple("c", ["part", "hi"])
g = namedtuple("bite", "teeth u y")
h = g(8,9,34)
d = c("point", "killer")
b = d[0] + d[1]
b = h.u + h.teeth - h.y
h._
print(b)

li = [1,2,3,4,5,6,7,7,8,8,9,9,9,4,6,0]
dic = {"a": 1, "b": 5}
tup = (1,2,3,44,8,5,5,5,5,55,4,7,3,2,2,4,5,5,5)
se = {1,2,3,4,5,5,6}
c = Counter()
c.update(se)
b = Counter(li)
c.subtract(b)
c= c + b
c = c.most_common()
c = b
#c.clear()
c = list(b.elements())
print(c)

f = open("sample.txt", "r")
data = f.read()
b = data.split()
c = Counter(b)
c = c.most_common(2)
n = []
for x in c:
    n.append(x[0])
print(n)
"""

"""row = 3
coloumn = 3

for i in range(row):
    for _ in range(coloumn - i):
        print("  ", end="")
    for _ in range(i + 1):
        print("# ", end="")
    for _ in range(i):
        print("# ", end="")
    print()

for i in range(row - 1):
    for _ in range(i + 2):
        print("  ", end="")
    for _ in range((coloumn - 1) - i):
        print("# ", end="")
    for _ in range((coloumn - 2) - i):
        print("# ", end="")
    print()"""

"""from dialog import DialogReader as dr
# AssignVariables
n = "hello"
m = "eLEphAnt"
n = dr.dialog("fisrt section typing a random word")
m = dr.dialog("second section typing a random word")
li = []
caps = []

# FirstSection
li = sorted(list(n.lower()))
n = "".join(li)
print(n)

# SecondSection
li = sorted(list(m.lower()))
for c in m:
    if c.isupper():
        caps.append(c)
m = ""
for l in li:
    if caps.count(l.upper()) != 0:
        m += l.upper()
        caps.pop(caps.index(l.upper()))
    else:
        m += l
print(m)"""
"""
matc = [
    [4,6,2],
    [2,4,6],
    [6,2,4]
]
"""
"""matc = [
    [1,2,3,4],
    [2,4,1,3],
    [3,1,4,2],
    [4,3,2,1]
]"""

"""matc = [
    [2,2,2],
    [2,2,2],
    [2,2,2]
]"""

"""matc = [
    [12,3,4,5],
    [5,67,8,9],
    [102,3,4,6],
    [34,2,89,0]
]"""
"""
def check_magic(matric, is_magic : bool = False, show_len = True, show_sum =False):
    li = []
    ly = []

    length = len(matric)

    for i in range(len(matric)):
        li.append(sum(matric[i]))

    for j in range(len(matric)):
        for i in range(len(matric[j])):
            ly.append(matric[i][j])
        li.append(sum(ly))
        ly = []

    for y in range(2):
        for i in range(len(matric)):
            for j in range(len(matric[i])):
                if j == i and y == 0:
                    ly.append(matric[i][j])
                if j == (length - 1) - i and y == 1:
                    ly.append(matric[i][j])
        li.append(sum(ly))
        ly = []

    if show_len:
        print(f"length is: {length}")
    if show_sum:
        print(f"The sum of the each row, column, diagonal is: {li[0]}")
    if is_magic:
        print(li)

    for i in range(len(li)):
        if li[i] != li[i - 1] and i != 0:
            print("matric is not a magic square")
            break
    else:
        print("matric is a magic square")

check_magic(matc,show_sum=True)
"""

"""
import cv2

img = cv2.imread("asset/opp.jpg", 1)
img = cv2.resize(img, (0,0), fx= 0.25, fy= 0.25)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite("asset/logo.jpg", img)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
"""
import cv2
import random as rd

img = cv2.imread("asset/opp.jpg", 1)
img = cv2.resize(img, (0,0), fx= 0.25, fy= 0.25)

tag = img[125:163, 150:200]
tag = cv2.rotate(tag, cv2.ROTATE_90_COUNTERCLOCKWISE)
img[50:100 , 100:138] = tag

print(img.shape)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
"""
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
shrink = 0.5

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(0, 0), fx= shrink, fy= shrink)
    width = int(cap.get(3) * shrink)
    height = int(cap.get(4) * shrink)

    image = np.zeros(frame.shape, np.uint8)
    sml_frame = cv2.resize(frame,(0, 0), fx= 0.5, fy= 0.5)
    image[:height// 2, :width // 2] = cv2.rotate(sml_frame, cv2.ROTATE_180)
    image[height// 2:, :width // 2] = sml_frame
    image[:height// 2, width // 2:] = cv2.rotate(sml_frame, cv2.ROTATE_180)
    image[height// 2:, width // 2:] = sml_frame
    
    cv2.imshow("Frame", image)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
"""
"""
import numpy as np
import cv2

cap = cv2.VideoCapture("asset/amongus.mp4")
shrink = 0.125

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(0, 0), fx= shrink, fy= shrink)
    width = int(cap.get(3) * shrink)
    height = int(cap.get(4) * shrink)

    img = cv2.line(frame,(0, 0), (width, height), (255, 0, 0), 5)
    img = cv2.line(img,(0, height), (width, 0), (0, 255, 0), 5)
    img = cv2.rectangle(img, (50, 50), (100, 100), (0, 0, 255), 2)
    img = cv2.circle(img, (200, 50), 50, (20, 20, 20), -1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, "Peter's awesome", (200, height - 10), font, 1,(0, 0, 0), 2, cv2.LINE_AA)
    
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
"""

"""
bgr_colour = np.array([[[255, 0, 0]]])
x = cv2.cvtColor(bgr_colour,cv2.COLOR_BGR2HSV)
x[0][0]
"""
"""
import numpy as np
import cv2

cap = cv2.VideoCapture("asset/amongus.mp4")
shrink = 0.125

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(0, 0), fx= shrink, fy= shrink)
    width = int(cap.get(3) * shrink)
    height = int(cap.get(4) * shrink)
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    result = cv2.bitwise_and(frame, frame, mask= mask)

    cv2.imshow("Frame", result)
    cv2.imshow("Mask", mask)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
"""
"""
import numpy as np
import cv2

img = cv2.imread("asset/opp.jpg", 1)
img = cv2.resize(img, (0, 0), fx= 0.25, fy= 0.25)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 20, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 2, (0, 0, 255), -1)

for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 1)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

"""n = 103466645
print(sum(range(n)))
print((n * (n-1)) // 2)"""

"""x = [i*j for i in range(10)for j in range(i*10) if i % 2 == 0]
y = [[0 for _ in range(5)]for _ in range(5)]
i = (u for u in "hello")
i = tuple(i)
o =[4] * 5
p = [4 for _ in range(5)]
a = 1 if 2 > 3 else 0
b = list(zip(o, p))
for n, m in zip(o, p):
    if m == n:
        pass
li = [[6,7], [4,8], [-1,3], [1,2]]
li.sort(key=lambda x: x[1])
import itertools
sum_i = list(itertools.accumulate(o))
li2 = list(itertools.chain(sum_i, o))
li3 = list(itertools.compress(sum_i, [0,1,0,1]))
k = b"hello"
print(k)"""

import pickle
import pandas as pd
from sklearn import preprocessing, model_selection
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from matplotlib import pyplot as plt

csv = r"SongMusicData\allArtistMetrics.csv"
data = pd.read_csv(csv)
names = []
song = []
for x in data["Artist"]:
    if x not in names:
        names.append(x)
for x in data["Album"]:
    if x not in song:
        song.append(x)
#Name,ReleaseDate,Label,Album,pop1,pop2,pop3,pop4,nonBandMemberWriters,lyricalComplexity,musicalComplexity,totalComplexity,Artist
le = preprocessing.LabelEncoder()
artist = le.fit_transform(list(data["Artist"]))
song_name = le.fit_transform(list(data["Name"]))
album = le.fit_transform(list(data["Album"]))
#predict = "pop4"
predicter = data["Artist"]
data = data[["pop4", "pop1", "pop2", "pop3", "lyricalComplexity", "musicalComplexity", "totalComplexity"]]
#val = np.array(data.drop([predict], 1))
val = np.array(data)

x = np.zeros((262, 9))
x[:, :7] = val
x[:, 7] = song_name
x[:, 8] = album
#y = np.array(data[predict])
y = artist
train = 0
test_acc = 0.15

x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size= test_acc)

if train:
    best = 0
    times_to_train = 100
    for i in range(times_to_train):
        x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size= test_acc)
        classifer = KNeighborsClassifier(n_neighbors= 7)
        classifer.fit(x_train, y_train)
        acc = classifer.score(x_test, y_test)
        if acc > best:
            best = acc
            with open("song_model.pickle", "wb") as Data:
                pickle.dump(classifer, Data)
            with open("song_data_accuracy", "w") as f:
                f.write(str(best))
else:
    with open("song_model.pickle", "rb") as Data:
        classifer = pickle.load(Data)
    with open("song_data_accuracy", "r") as f:
        acc = f.read()
        
    print("Accuracy:", acc)
    predictions = classifer.predict(x_test)
    """for x in range(len(predictions)):
        print("Prediction:", names[int(predictions[x])], "Data:", "{", x_test[x][:8], song[int(x_test[x][8])], " }", "Actual_value:", names[int(y_test[x])])
"""
    p = "musicalComplexity"
    lic = []
    lis = []
    for _ in range(256):
        lic.append(np.random.randint(0, 256))
        lis.append(np.random.randint(0, 100))

    plt.figure(figsize=(12, 5))
    plt.scatter(predicter, data[p], s= lis, c= lic)
    plt.show()