from random import randint, choice, randrange
import numpy as np
from dialog import correction as cor
from dialog import DialogReader as dr

create = 50#int(dr.dialog("Inupt a number", quiter=False, error_type= "numb"))
cont = {}
f_names = ["horn", "lava", "dark", "fire", "void", "karma", "calamity"]
l_names = ["dear", "bear", "wolf", "boar", "dragon", "goat", "dear", "cat", "horse"]
for _ in range(create):
    age = randint(0, 100)
    START_START = 15
    name = choice(f_names).capitalize() + "" + choice(l_names).capitalize()
    stats = {"Hp" : 0, "Att" : 0, "Spd" : 0, "Spat": 0, "Lck" : 0}
    clas = list(stats.keys())
    affinity = [clas[randint(0, len(clas) - 1)], 5]
    stat = START_START - affinity[1]
    r = np.zeros(len(stats))
    envir = choice(["peace", "war"])
    luck = randrange(100, 1000, 5)
    exprt = 50
    dis_stat = 4
    maxexpr = exprt
    lvl = -1

    while stat:
        if stat // len(clas) == 0:
            break
        div = stat // len(clas)
        stats = {i : randint(0, div) for i in clas}
        r += (list(stats.values()))
        stat -= sum(stats.values())
    stats = {i :r[j] for j, i in enumerate(clas)}
    stats[affinity[0]] += affinity[1]
    choos = clas[randint(0, len(clas)-1)]

    if stat < len(clas) and stat > 0:
        stats[choos] += stat
        stat = 0
    if envir == "peace":
        yrs = round(age - (5 * 1.5))
    else:
        yrs = round(age - (5 / 1.5))
    expr = yrs * luck * exprt

    while True:
        lvl += 1
        prev = exprt
        if expr > exprt:
            maxexpr *= 1.2
            exprt = round(maxexpr)
            exprt += prev
        else:
            exprt -= expr
            break

    maxexpr = round(maxexpr)
    stats = {clas[j] : round(i/START_START * 100) for j, i in enumerate(stats.values())}
    base = {clas[j] : round(i/START_START * 100) for j, i in enumerate(stats.values())}
    dis_stat *= lvl
    for j, i in stats.items():
        stats[j] = round((i/ 100) * dis_stat)
    stats = {i: j + 1 for i, j in stats.items()}
    hunt = stats["Att"] + stats["Spd"] + stats["Spat"]
    survive = stats["Hp"] + stats["Spd"] + stats["Lck"]
    cont["0" + str(len(cont))] = [["name", name], ["lvl", lvl], ["age", age], ["stats", stats, base], ["survivablity", survive], ["hunt", hunt], ["yrs/expr/maxexpr", yrs, maxexpr, expr]]

# Experence
def expence(ent = 0, en = 1):
    """
    output is:
    expr  6, 2
    max   6,3
    level 1,1
    stats 3,1
    """
    lvl = cont[f"0{ent}"][1][1]
    maxexpr = cont[f"0{ent}"][6][2]
    exprt = maxexpr
    stats = cont[f"0{ent}"][3][1]
    expr = cont[f"0{en}"][6][1] * cont[f"0{en}"][4][1] * cont[f"0{en}"][1][1]
    while True:
        prev = exprt
        if expr > exprt:
            maxexpr *= 1.2
            exprt = round(maxexpr)
            exprt += prev
        else:
            exprt -= expr
            break
        lvl += 1
    maxexpr = round(maxexpr)
    dis_stat = lvl - cont[f"0{ent}"][1][1]

    for j, i in cont[f"0{ent}"][3][2].items():
        stats[j] += round((i/ 100) * dis_stat)
    hunt = stats["Att"] + stats["Spd"] + stats["Spat"]
    survive = stats["Hp"] + stats["Spd"] + stats["Lck"]

    return [cont[f"0{ent}"][0], ["lvl", lvl], cont[f"0{ent}"][2],["stats", stats, cont[f"0{ent}"][3][2]], ["survivablity", survive], ["hunt", hunt], ["yrs/expr/maxexpr", cont[f"0{ent}"][6][1], exprt, maxexpr]]

# Fight Section
nature = 200
died = []
fin = False
lent = len(cont) - 1
for _ in range(nature):
    while True:
        att = randint(0, lent)
        hp = randint(0, lent)
        if len(died)+ 1  == lent:
            fin = True
        if (f"0{hp}" not in died and f"0{att}" not in died) or fin == True:
            break
    if fin == True:
        break
    if cont[f"0{hp}"][4][1] > cont[f"0{att}"][5][1]:
        if cont[f"0{att}"][4][1] > cont[f"0{hp}"][5][1]:
            cont[f"0{hp}"] = expence(hp, att)
            #print(cont[f"0{hp}"][0][1], "Killed!", cont[f"0{att}"][0][1])
            died.append(f"0{att}")
            cont.pop(f"0{att}")
        else:
            #print(cont[f"0{hp}"][0][1], "survived")
            pass
    else:
        #print(cont[f"0{att}"][0][1], "Killed!", cont[f"0{hp}"][0][1])
        cont[f"0{att}"] = expence(att, hp)
        died.append(f"0{hp}")
        cont.pop(f"0{hp}")

print(len(cont))
for i in cont:
    #print(cont[i][0], cont[i][3])
    print(cont[i])