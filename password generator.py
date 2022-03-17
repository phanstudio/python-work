from dialog import DialogReader as dr
import random as rd

while True:
    length = dr.dialog("Input the length of the password",quiter= False, error_type=["numb"])
    special_char = dr.dialog("Should the password have special charcters Yes[Y] or No[N]",quiter= False, error_type=["numerical"])
    numb = dr.dialog("Should the password have numbers Yes[Y] or No[N]",quiter= False, error_type=["numerical"])

    # Assigning variables
    length = int(length)
    numb_div = 0
    special_div = 0
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    numbers = [0,1,2,3,4,5,6,7,8,9]
    symbols = ["#","%","$"]
    password_db = []
    password = ""
    li = []
    ly = []

    if numb[0].lower().strip() == "y":
        # Number
        numb_div = round(length / 3)
        for _ in range(numb_div):
            i = rd.randrange(0, (length - 1))
            li.append(i)

    if special_char[0].lower().strip() == "y":
        # Special Character
        special_div = round((length - numb_div) / 4)
        for _ in range(special_div):
            while True:
                i = rd.randrange(0, (length - 1))
                if not i in li:
                    ly.append(i)
                    break

    #letters
    for _ in range(length):
        j = rd.randint(0, len(letters)- 1)
        password_db.append(letters[j])

    #numbers
    for x in li:
        y = rd.randint(0, len(numbers)-1)
        password_db[x] = numbers[y]

    #synbols
    for x in ly:
        y = rd.randint(0, len(symbols)-1)
        password_db[x] = symbols[y]

    for g in password_db:
        password = password + str(g)
    print(password)

    user_yn = dr.dialog("Do you want to generate another code? Yes[Y] or No[N]",quiter= False, error_type=["numerical"])
    if user_yn[0].lower().strip() == "y":
        continue
    else:
        print("Thank you!")
        break
