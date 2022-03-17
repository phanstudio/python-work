import random as rd
from dialog import DialogReader as dr
difficulty = 1
rang = 10
norm = rang
guess_min = 5

while True:
    correct = False
    numb_of_guesses = 0
    numb = rd.randrange(0, rang)
    print(f"Level {difficulty}")
    while True:
        print(f"{guess_min - numb_of_guesses} chances")
        anwser = int(dr.dialog(f"guess which number from 0 - {rang}?\n", quiter= False, error_type=["numb"]))
        if anwser == numb:
            print("you guessed correctly!")
            correct = True
            break
        if anwser > numb:
            print("you guessed higher than the number")
        if anwser < numb:
            print("you guessed smaller than the number")
        if numb_of_guesses == guess_min:
            print("you used up your guesses, you lost!")
            break
        numb_of_guesses += 1
    
    if correct == True:
        print(f"correct number({numb})")
        useryn = dr.dialog("Do you want to progress/continue[P/C] or retry[R] or ")
        if useryn == "":
            useryn = "p"
        useryn = useryn[0].lower()
        if useryn == "p" or useryn == "c":
            if difficulty % 10 == 0:
                norm += norm
            difficulty += 1
            if difficulty % 2 != 0:
                guess_min += 1
            rang = norm * difficulty
        if useryn == "r":
            continue
    else:
        contyn = dr.dialog("Do you want to try again yes[Y] or no[N]", quiter= False)
        if contyn == "":
            contyn = "y"
        contyn = contyn[0].lower()
        if contyn == "y":
            continue
        elif contyn == "n":
            break
