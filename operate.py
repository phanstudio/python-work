import random as rd
import time 

class Car:
    def __init__(self, name:str, top_speed = 50, accel = 5, drag = 10, breaker = 5, driver= 5, nitro = 10, noss = 2) -> None:
        self.spd = 0.1
        self.dist = 0
        self.turn = 0
        self.time = 0 
        self.curve = 0
        self.n_dist = 0
        self.noss = noss
        self.name = name
        self.drag = drag
        self.accel = accel
        self.nitro = nitro
        self.driver = driver
        self.top = top_speed
        self.in_curve = False
        self.use_noss = False
        self.breaker = breaker
        self.top_speed = top_speed
        self.n_drag = self.drag / (self.drag / 6)
        self.speed = ((self.accel / self.drag) + (self.driver / self.drag))
        self.deccel = round((self.drag * self.breaker) / (self.top_speed / self.speed))

    def __repr__(self) -> str:
        return str(self.name).capitalize() + " Car"

def race_track(*rl, distance = 1000, curve = 4):
    # Setting variables
    n = ""
    u = ""
    g = {}
    l = {}
    li = []
    ly = []
    ry = []
    v = set()

    # selecting when to use noss
    for r in rl:
        r.n_dist = rd.randint(200, distance)
        ry.append(r.top_speed)

    # Defining the curve
    for i in range(curve):
        g[curve - i] = rd.randint(3, 10)
        l[curve - i] = rd.randint(1, g[curve - i])
    for r in rl:
        r.curve = curve
        ly.append(r.speed)
    li = [7,8,9,10]#func2(ly, dis= distance, cu= curve)
    #print(li)

    # Main Game loop
    for r in rl:
        n += (r.name.capitalize() + " Car vs ")
        u += (r.name.capitalize() + " Car  ")
        pass
    n = "(" + n[:-4] + ")"
    u = "(" + u[:-2] + ")"
    print(f"Welcome to the race {n}")
    time.sleep(2)
    print(u)
    while True:
        for r in rl:
            #print(r.curve)
            if not r.in_curve:
                # Moving outside the Curve
                if r.use_noss:
                    if r.nitro > 0:
                        noss = r.noss
                        r.top_speed =  r.top * (noss / (r.driver / (r.drag - r.n_drag)))
                        r.speed = ((r.accel / r.drag) + (r.driver / 5)) * (noss + round((r.driver + 1) / r.drag))
                        r.nitro -= 1
                    else:
                        r.top_speed =  (r.top + (r.driver // r.drag))
                        r.speed = (((r.accel / r.drag) + (r.driver / 5)) + (r.driver / r.drag))
                        r.use_noss = False
                if r.spd < r.top_speed:
                    r.spd += r.speed
                else:
                    r.spd = r.top_speed
            else:
                # Moving inside the Curve
                curve_str = g[r.curve]
                slop = l[r.curve]
                curve_speed = round(((r.top_speed + r.driver) / (curve_str + slop)))
                if r.spd > curve_speed:
                    r.spd -= r.deccel
                else:
                    r.spd = curve_speed
                    
                if curve_str > r.turn:
                    r.turn += 1
                else:
                    r.turn = 0
                    #print(f"{r}({r.dist}) aft: {curve_speed}")
                    #print(curve_str)
                    if r.curve > 1:
                        r.curve -= 1
                    r.in_curve = False
            
            #Checking if a curve appears
            if r.in_curve == False:
                #print(r.curve)
                for i in range(int(li[((len(li) - 1) - (r.curve - 1))] - 40), int(li[((len(li) - 1) - (r.curve - 1))] + 40)):
                    if r.dist == i:
                        #print(r.curve - 1)
                        #print(f"{r}( {r.dist} ) bef: {(r.curve - 1)}")
                        #print(li)
                        #r.in_curve = True
                        pass
            #print(r.curve)
            """if r.in_curve == False:
                #print(r.dist)
                for i in range(int(li[(r.curve - 1)] - 30), int(li[(r.curve - 1)] + 30)):
                    if r.dist == i:
                        print(li[(r.curve - 1) - (len(li) - 1)])
                        print(li[0])
                        print(li)
                        r.in_curve = True"""
            
            # Checking the nostime
            if r.use_noss == False:
                n = sum(ry) / 2
                for j in range(int(r.n_dist - n), int(r.n_dist + n)):
                    if r.dist == j:
                        r.use_noss = True

            # The distance Checker
            if distance > r.dist:
                r.dist += r.spd
                r.time += 1
            else:
                v.add(r)
            if int(r.spd) != 0 and not r in v:
                print(int(r.spd), ".mile/s" , end= " ")
                pass
        print()
        
        # Win Condition
        if len(v) == len(rl):
            win = []
            best = rl[0].time
            for r in rl:
                print(r, "finishing in", str(r.time), "secends")
                if r.time < best:
                    best = r.time
                    win = r
            print(win, "is the winner of the race")
            break

def func2(rl: list, dis = 500, cu = 5):
    r = sum(rl)
    time = int(dis / (r / len(rl)))
    li = []
    ly = []
    incr = 5 #500
    x = 1
    for _ in range(cu):
        x = rd.randrange(20, time - 20, incr)
        while True:
            if not x in li:
                if x in ly:
                    ly.remove(x)
                li.append(x)
            else:
                while x in li:
                    x += (incr + 10)
                    if x >= (time - 20):
                        x = 40
                ly.append(x)
            if ly == []:
                break
    li.sort()
    return li

c = Car("top", accel= 5, drag= 20)
b = Car("pot", 70)
a = Car("opp", accel= 10, drag= 4)
g = Car("lot", 40, drag= 2)
l = Car("nlp", accel= 15)
p = Car("ptt", 90, accel= 2)
race_track(c, b, a, g, l, p, distance= 10000)

"""
#Static and class methods
from math import trunc
import random
class Car(object):
    accel = 10
    deccel = 6
    timer = 0
    start = 0
    dis = 0
    in_curve = False
    def __init__(self, name, ms = 20):
        self.name = name 
        self.ms = ms
        self.mms = ms
        if self.ms >= 20:
            print("You created a car called", self.name + ", it runs at", self.mms, "miles per hour")
        else:
            print("that car can not run ms is too small...! increase it above 200miles")
    def race(self, drag = 10, start = 0):
        self.accel = self.mms / drag
        self.deccel = self.mms / (drag + 4)
        self.start = start
        self.in_curve = False
    def race_time(self, timer = 0, dis = 0):
        self.timer = timer
        self.dis = dis
"""
"""
def func(racer1, racer2, distance = 4000, curves = 3, start1 = 0, start2 = 0):
    accel1 = racer1.accel
    accel2 = racer2.accel
    deccel1 = racer1.deccel
    deccel2 = racer2.deccel
    racer1.ms = 0
    racer2.ms = 0
    timer1 = racer1.timer
    timer2 = racer2.timer
    li = func2(distance,racer1,racer2, curves)
    print("0" + str(racer1.ms), "0" + str(racer2.ms))
    while True:
        if racer1.ms < racer1.mms:
            racer1.ms += accel1
        else:
            racer1.ms = racer1.mms
        if racer2.ms < racer2.mms:
            racer2.ms += accel2
        else:
            racer2.ms = racer2.mms
        if start1 < distance:
            start1 += racer1.ms
            timer1 += 1
        if start2 < distance:
            start2 += racer2.ms
            timer2 += 1
        #print(int(start1), int(start2))
        print(int(racer1.ms), int(racer2.ms))
        for x in li:
            if timer1 == x:
                slop = 0
                slop_str = random.randint(2, 10)
                while True:
                    curve = random.randint(2, slop_str)
                    if racer1.ms >= (racer1.mms / curve):
                        racer1.ms -= deccel1
                    if slop < slop_str:
                        if start1 < distance:
                            start1 += racer1.ms
                            timer1 += 1
                            slop += 1
                        if start2 < distance:
                            start2 += racer2.ms
                            timer2 += 1
                        #print(int(start1), int(start2))
                        print(int(racer1.ms), int(racer2.ms))
                    elif slop == slop_str:
                        break
        if start1 >= distance and start2 >= distance:
            break
    if timer1 < timer2:
        print(racer1.name, "is the winner of the race, finishing in",
             timer1, "secends")
        print(racer2.name, "lost of the race, finishing in", timer2, "secends")
    elif timer1 > timer2:
        print(racer2.name, "is the winner of the race, finishing in",
             timer2, "secends")
        print(racer1.name, "lost of the race, finishing in", timer1, "secends")
    else:
        if start1 > start2:
            print(racer1.name, "is the winner of the race, finishing in",
                timer1, "secends")
            print(racer2.name, "lost of the race, finishing in", timer2, "secends")
        elif start1 < start2:
            print(racer2.name, "is the winner of the race, finishing in",
                timer2, "secends")
            print(racer1.name, "lost of the race, finishing in", timer1, "secends")
        else:
            print("it was a tie no winner")
"""
"""      

def func(racer1, racer2, distance = 4000, curves = 3):
    racer1.ms = 0
    racer2.ms = 0
    li = func2(distance,racer1,racer2, curves)
    print(li)
    print("0" + str(racer1.ms), "0" + str(racer2.ms))
    func3(distance, li, racer1, racer2)

def func2(dis, r1, r2, cu):
    time = int(dis / ((r1.mms + r2.mms) / 2))
    li = []
    x = 1
    for _ in range(cu):
        #x = random.randint(x, (time - 20))
        x = random.randrange(20, time - 20, 10)
        li.append(x)
    li.sort()
    return li

def func3(dis, li, *rn):
    p1 = []
    finished = []
    while True:
        for r in rn:
            if r.ms < r.mms:
                r.ms += r.accel
            else:
                r.ms = r.mms
            if r.start < dis :
                r.start += r.ms
                r.timer += 1
                r.dis += 1
            if not (str(int(r.start)) + " ")in p1:
                p1.append(str(int(r.start)) + " ")
            if r.start >= dis:
                if not r in finished:
                    finished.append(r)
                    print(len(finished))
                if len(finished) >= 2:
                    break
        p= "".join(p1)
        print(p)
        p1.clear()
        func4(li, func5(rn), dis)

def func4(li, rn, dis):
    curved = False
    p1 = []
    p2 = []
    p3 = []
    pl = []
    slop = 0
    slop_str = random.randint(2, 10)
    for x in li:
        for r in rn:
            if r.dis == x:
                #print(slop_str)
                while True:
                    curve = random.randint(2, slop_str)
                    if r.ms >= (r.mms / curve):
                        r.ms -= r.deccel
                    if slop < slop_str:
                        if r.start < dis:
                            r.start += r.ms
                            r.timer += 1
                            r.dis += 1
                            slop += 1
                    if not (str(int(r.ms)) + " ")in p1:
                        p1.append(str(int(r.ms)) + " ")
                    if slop == slop_str:
                        curved = True
                        break
            elif curved == True:
                recover = 0
                while True:
                    if r.in_curve == False:
                        if recover < slop_str:
                            r.start += r.ms
                            r.timer += 1
                            r.dis += 1
                            recover += 1
                        if not (str(int(r.ms)) + " ")in p2:
                            p2.append(str(int(r.ms)) + " ")
                        p= "".join(p2)
                        p3.append(p)
                        p2.clear()
                        if recover == slop_str:
                            curved = False
                            break
            if r.in_curve:
                r.in_curve = False
            for _ in range(slop_str):
                if p1 and p2:
                    n = str(p1.pop() + p2.pop() + "\n")
                    pl.append(n)
            if pl:
                p = "".join(pl)
                print(p)
                pl.clear()

def func5(*it):
    y = []
    li = []
    for x in it:
        y = x
        for i in y:
            if not i in li:
                li.append(i)
        return li

mos1 = Car("corola",30)
mos1.race(2)
mos1.race_time()

mos2 = Car("corolana",35)
mos2.race(6)
mos2.race_time()
func(mos1, mos2, 5000)
"""
"""
class person(object):
    population = 50
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def get_population(cls):
        return cls.population
    @staticmethod
    def is_adult(age):
        return age >= 18
    def display(self):
        print(self.name , "is", self.age, "years old")
"""

"""
class Dog:
    def __init__(self,dogName,dogAge) -> None:
        self.dogName = "NA"
        self.dogAge = "NA"
        print("My dogs name is " + dogName + " and it's " + str(dogAge) + " years old")
        pass
    
    def bark(self):
        print("wooof...!")
    pass

def main():
    mydog = Dog("steve", 6)
    mydog.bark()

    mycat = Dog("boy", 3)
    pass

main()
"""
class Ink():
    def __init__(self, x: int) -> int:
        self.x = x
    def __add__(self, x):
        return "Ink(" + str(self.x + x.x) + ")"
    def __str__(self) -> str:
        return "Ink(" + str(self.x) + ")"

i = Ink(2)
b = Ink(3)
"""print(i)
print(i + b)"""