#from collections import Counter 

"""
import random

while True:
    try:
        loop = int(input("input number of times you want to run this code: "))
        break
    except:
        print("input the a number,try again")
for _ in range(loop):
    numb = random.randint(1, 1000)

    print(numb)
"""


"""
while True:
    try:
        numb = int(input("input number to find it's factorial: "))
        break
    except:
        print("input the a number,try again")
fNumb = 1
for fac in range(1, numb+1):
    fNumb *= fac
    if fac == (numb):
        print(str(numb) + " factorial is " + str(fNumb))
"""


"""
countinue = True
while countinue:
    while True:
        try:
            numb = int(input("input number check if it is a prime number: "))
            break
        except:
            print("input the a number,try again")

    if numb == 1:
        print(numb + "is a prime number")
    else:
        for div in range(1, numb):
            if numb % div == 0 and div != 1:
                print("it is't a prime number")
                break
            elif div == (numb - 1) :
                print("it is a prime number")

    userYN = input("Do you want to continue the game Yes[Y] or No[N]? ")
    if userYN[0].lower().strip() != "y" :
        countinue = False
        break
    else:
        continue
"""



"""
lt = [23, 54, 78, 99, 67, 999, 576, 100, 78, 5, 99, 5, 7955758, 549, 57594, 757]

print(max(lt))
"""

"""
while True:
    try:
        numb = int(input("type a number here: "))
        break
    except:
        print("write the correct number")
if (numb % 2) == 1:
    print("odd number")
else:
    print("even number")
"""


"""
import heapq

grades = [7,9,76,87,55,87,90,45,87]
print(heapq.nlargest(3,grades))
stocks =[
    {"ticker":"appl", "price":201},
    {"ticker":"goog", "price":2001},
    {"ticker":"cili", "price":71},
    {"ticker":"aplp", "price":91},
]


print(heapq.nsmallest(2,stocks,key=lambda stock : stock["price"]))
"""

"""
x = 9 
z = 17
y = x | z
print(y)

bob = {"face" : 689, "goog": 89, "pow" : 7}
minValue = min(zip(bob.values(), bob.keys()))
print(minValue)
"""

"""
from struct import *

packedData = pack('iif', 6, 19, 4.73)
print(packedData)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

unpackedData = unpack('iif', packedData)
print(unpackedData)
"""

"""
import sorter

sorter.start_sort("sample.txt")
"""

"""
from PIL import Image

img = Image.open("2001214.jpg")
area =(100, 600, 900, 1500)
cropImg = img.crop(area)
r, g, b = cropImg.split()
newImage = Image.merge("RGB", (b, g, r))
resizeImage = newImage.resize((250,250))
resizeImage.show()
#img.show()
#cropImg.show()
"""


"""
game = ["how", "are", "you", "now"]
level = ["I", "am", "fine", "yeah"]

hp, jump, *att, spd = [20, 9, 8, 5, 7]
print(jump)

bobo = zip(game, level)

for a, b in bobo:
    print(a,b)
"""


"""
import threading

class messager(threading.Thread):
    def run(self) -> None:
        for _ in range(10):
            print(threading.currentThread().getName())
        #return super().run()

x1 = messager(name="Send out message")
x2 = messager(name="Recieve message" )
x1.start()
x2.start()
"""


"""
import requests
from bs4 import BeautifulSoup

def trade_spider(maxPage):
    page = 1
    while page <= maxPage:
        url = r"https://codeclubng.com/"
        sourceCode = requests.get(url)
        plainText  = sourceCode.text
        soup = BeautifulSoup(plainText)
        for link in soup.find_all('a', {"class":"item.name"}):
            href = link.get("href")
"""


"""
from urllib import request

googUrl = "https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1599461629&period2=1630997629&interval=1d&events=history&includeAdjustedClose=true"

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csvStr = str(csv)
    lines = csvStr.split("\\n")
    destUrl = r"goog.csv"
    fx = open(destUrl, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_stock_data(googUrl)
"""

"""
Fw = open("sample.txt", "w")
Fw.write("you are a vagina, i am awesome \n")
Fw.write("you are soo awesome\n")
Fw.close()

Fr = open("sample.txt", "r")
text = Fr.read()
print(text)
Fr.close()
"""

"""
import random
import urllib.request

def download_wed_image(url):
    name = random.randrange(1, 1000)
    fullName = str(name) + ".jpg"
    urllib.request.urlretrieve(url, fullName)

download_wed_image("https://previews.123rf.com/images/firdausexia/firdausexia1303/firdausexia130300002/18236451-only-one-tress.jpg")
"""

"""
for i in range(0,101,2):
    if i % 4 == 0:
        print(i)

def lick(n = 1, m = 2, k = 4):
    print(n,m,k)
    pass

lick(m = 7)

def kop(*argu):
    print(argu)

kop(3)
kop(3,8,9,"op")
"""

"""
import turtle

i = turtle.Turtle()
i.shape("turtle")
i.color('blue')
i.pensize(2)
for _ in range(4):
    i.left(90)
    i.forward(100)
i.left(45)
i.forward(200)
i.left(45)
i.forward(100)
i.right(45)
i.backward(200)
i.penup()
i.right(45)
i.backward(100)
i.pendown()
i.showturtle()
i.left(45)
i.forward(200)
i.right(45)
i.forward(100)
i.hideturtle()

while True:
    m = input(": ")
    if m == "":
        break
"""

"""
while True:
    #calculate = "9+5*5/6+9"
    #calculate = "5/5+6"
    calculate = "5+5/5/9+6"
    j = 1
    t = 1
    b = 0
    a = 0
    length = 0
    num1 = ""
    num2 = ""
    operate = ""
    n = 0
    calc = ""
    c = ""
    done = ""
    h = True
    while h:
        for i in range(len(calculate)):
            print(calculate[i])
            if calculate[i] == "/":
                while (b != 1 or a != 1):
                    if i - (j + 1) != -1 and (calculate[i - (j + 1)] != "+"):
                        j += 1
                    else:
                        b = 1
                    if i + (t + 1) < len(calculate) and (calculate[i + (t + 1)] != "+"):
                        t += 1
                    else:
                        a = 1
                if calculate[i - (j + 1)] == "+":
                    if done != "":
                        calculate = calculate[:i - (j)] + "("+ calculate[i - (j):i + (t + 1)] + ")" + calculate[i + (t + 1):]
                    else:
                        calculate = calculate[:i - (j)] + done + calculate[i + (t + 1):]
                    #calc = calculate[i - (j-1):i + (t + 2)]
        print(calculate)

        for i in range(len(calculate)):
            if calculate[i] == "(":
                for j in range(len(calculate)):
                    if calculate[j] == ")":
                        calc =  calculate[(i+1):j]
                        break
        print(calc)
        if calc == "":
            c = calculate
        else:
            c = calc

        def div(x, y):
            return x / y
        for i in range(len(calculate)):
            if calculate[i] == "(":
                for j in range(len(calculate)):
                    if calculate[j] == ")":
                        for u in calculate[(i+1):j]:
                            if u == " ":
                                length += 1
                                continue
                            if operate != "" and (u == "/"):
                                break
                            if "/" == u:
                                operate = u
                                n = 1
                            elif n == 1:
                                num2 = num2 + u
                            else:
                                num1 = num1 + u
                            length += 1

        for i in c:
            if i == " ":
                length += 1
                continue
            if operate != "" and (i == "+" or i == "*" or i == "/" or i == "-"):
                break
            if "+" == i or "*" == i or "/" == i or "-" == i:
                operate = i
                n = 1
            elif n == 1:
                num2 = num2 + i
            else:
                num1 = num1 + i
            length += 1

        calc = calc[length:]

        if calculate == "":
            h = False
        operation = operate
        if operation == "/":
            sum = round(div(int(num1), int(num2)))
            print(sum)
        calc = str(sum) + calc
        print(calc)
        if not "/" in calc:
            done = calc
"""
while False:
    import time
    import playsound

    clock = 0
    alarm = "10:09:00"
    song = "_Drop.mp3"

    p = time.time()
    print(time)
    print(p)
    """while True:
        if time.ctime() == f"Wed Oct 27 {alarm} 2021":
            print("work")
            playsound.playsound(song)
            break
        else:
            pass

    print(time.ctime())
    print(f"Dur: {round(time.time() - p, 4)}Sec")"""
