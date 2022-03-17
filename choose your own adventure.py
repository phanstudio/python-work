from dialog import DialogReader as dr
import json

with open("choice.json", "r") as f:
    data = json.load(f)
path_gb = "morning"
karma_gb = 0
story = 0

print("You are a noble boy in this world")
question = dr.dialog("What is your name?")
name = question.lower().strip()
print("...")

while True:
    n_path = ""
    text = ""
    i = ""
    li = []
    numb = False

    for choices in data["choices"]:
        if choices["path"] == path_gb:
            questions = choices["question"]
            choice = choices["choice"]
            karma = int(choices["karma"])
            path = choices["path"]
            if "next" in choices:
                n_path = choices["next"]

    for t in questions:
        text = text + t + "\n"
    text = text[:-1]
    if r"{name}" in text:
        text = text.replace(r"{name}", name.capitalize())
    print(text)
    for c in choice:
        i = i + f"[{c[0]}[{c[0][0].upper()}]] "
        li.append(c)
    i = i[:-1]

    if n_path == "":
        if len(choice) == 0:
            break
        question = dr.dialog("What do you want to do?"+ "\n" + i + "\n", quiter= False)
        
        # Checks if the output is a number or the word or the first letter
        try:
            int(question)
            question = int(question)
            numb = True
        except:
            numb = False
        if numb == True:
            if question > (len(li) - 1):
                question = (len(li) - 1)
            c = li[question]
            story += 1
            if c[1] == "+":
                karma_gb += karma
                path_gb = "good" + str(story)
            elif c[1] == "-":
                karma_gb -= karma
                path_gb = "bad" + str(story)
            else:
                karma_gb += (karma * 0)
                path_gb = "neutral" + str(story)
        else:
            for c in choice:
                if question[:3].lower() in c[0][:3].lower():
                    story += 1
                    if c[1] == "+":
                        karma_gb += karma
                        path_gb = "good" + str(story)
                    elif c[1] == "-":
                        karma_gb -= karma
                        path_gb = "bad" + str(story)
                    else:
                        karma_gb += (karma * 0)
                        path_gb = "neutral" + str(story)
                elif question[0].lower() in c[0][0].lower():
                    story += 1
                    if c[1] == "+":
                        karma_gb += karma
                        path_gb = "good" + str(story)
                    elif c[1] == "-":
                        karma_gb -= karma
                        path_gb = "bad" + str(story)
                    else:
                        karma_gb += (karma * 0)
                        path_gb = "neutral" + str(story)

    else:
        path_gb = n_path

if karma_gb > 0:
    print("you are heading in a rightous path")
elif karma_gb < 0:
    print("you are heading in an evil path")
else:
        print("you are plain")
