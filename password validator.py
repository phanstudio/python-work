
def main():
    gameContinue = True
    while gameContinue:
        require = False
        strong = False
        hasSpecialSymbol = ["#","$","&"]
        hasNumber = ["0","1","2","3","4","5","6","7","8","9"]
        symbol = False
        special = False
        leng = False
        noChanges = True

        while not special:
            symbolYN = input("Should we use special symbols in the password Yes[Y] or No[N]: ")
            if symbolYN[0].lower() == "y":
                symbol = True
                special = True
            else:
                symbol = False
                special = True

        while not strong:
            try:
                passwordStrength = int(input("Choose the strenght of the password: "))
                if passwordStrength > 10:
                    strong = True
                else:
                    print("Too small...!")
            except:
                print("Input a number, try again")

        while not require:
            try:
                requiredLength = int(input("Write the required length of the password: "))
                if requiredLength > 6:
                    require = True
                else:
                    print("Too small...!")
            except:
                print("Input a number, try again")

        while noChanges:
            strength = 0
            length = False
            while not length :
                password = input("Input your password here: ")
                if len(password) >= requiredLength:
                    leng = True
                else:
                    print("Password is too small..!")
                cont = False
                symbols = False
                number = False
                required = False
                check = False
                hasError = True
                while not required:
                    if symbol == True:
                        for i in hasSpecialSymbol:
                            if i in password:
                                symbols = True
                        for i in hasNumber:
                            if i in password:
                                number = True
                        if symbols == True and number == True:
                            cont = True
                            required = True
                        else:
                            required = True
                            print("Password should have at least one number and one symbol, try again!")
                    else:
                        cont = True
                        required = True
                while not check:
                    if " " in password:
                        print("Password should not have spaces in it!")
                        check = True
                    else:
                        check = True
                        hasError = False
                if cont == True and leng == True and hasError == False:
                    strength += len(password)
                    length = True

            for i in hasSpecialSymbol:
                if i in password and symbol == True:
                    strength *= 2
            for i in hasNumber:
                if i in password and symbol == True:
                    strength *= 1.5

            if strength < passwordStrength / 2:
                print("Password is weak!")
            elif strength > passwordStrength:
                print("Password is Strong..!")
            else:
                print("Password is Ok")
            print(strength)
            userYN = input("Do you want to continue using the app Yes[Y] or No[N]? ")
            if userYN[0].lower() != "y" and userYN[:1].lower() != " y":
                gameContinue = False
                print("Thanks for using the app")
                break
            changeYN = input("Do want to change the parameters? Yes[Y] or No[N] ")
            if changeYN[0].lower() != "y" and changeYN[:1].lower() != " y":
                print("No changes")
                continue
            else:
                noChanges = False
                print("Lets keep going")
    pass

main()