import json
import random as rd
from dialog import DialogReader as dr

with open("questions.json", "r") as f:
    data = json.load(f)

quiz_li = []
anws_li = []
diff_li = []
score = 0
quest = []
numb_of_quest = 10

for i in range(len(data["questions"])):
    for j in data["questions"][i]:
        if j == "quiz":
            quiz_li.append(data["questions"][i][j])
        if j == "anwser":
            anws_li.append(data["questions"][i][j])
        if j == "difficulty":
            diff_li.append(data["questions"][i][j])

if numb_of_quest > len(quiz_li):
    numb_of_quest = len(quiz_li)

for i in range(numb_of_quest):
    while True:
        x = rd.randint(0, numb_of_quest - 1)
        if not x in quest:
            quest.append(x)
            break

#main loop 
while True:
    for i in quest:
        i = quiz_li[i]
        question = input(i + "?\n: ")
        question = question.lower()
        anwser = []
        correct = False
        s = 0
        for j in range(len(quiz_li)):
            if i in quiz_li[j]:
                li = []
                s = j
                for p in range(len(anws_li[j])):
                    u = ""
                    for y in anws_li[j][p].split():
                        u = u + " " + y[0]
                    li.append(u[1:].lower())
                for x in anws_li[j]:
                    x = x.lower()
                    anwser.append(x)
                    x = x.replace(" ", "")
                    anwser.append(x)
                for x in li:
                    anwser.append(x)
                    x = x.replace(" ", "")
                    anwser.append(x)
        for j in anwser:
            if question != "":
                if question in j:
                    correct = True
        if correct:
            print("correct anwser!")
            score += diff_li[s]
        else:
            print("wrong anwser!")

    div = numb_of_quest
    grade = str(round(((div - (div - score))/ div) * 100)) + "%"
    print(score , "/" , div)
    print(grade)

    contyn = dr.dialog("Do you want to continue?")
    if contyn[0].lower() == "n":
        break
