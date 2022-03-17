load = []

def lister(txt):
    li = []
    ly = []
    t = txt.split("\n")
    tx = ""
    for x in t:
        tx = x.split()
        li.append(tx)
    return li

def save_load(sl = "save", file = ""):
    global load
    if sl == "save":
        fs = open("login_sheet.txt", "r")
        sv = fs.read()
        save_file = open("login_sheet.txt", "w")
        if sv:
            save_file.write(str(sv + "\n" + file))
        else:
            save_file.write(file)
        print("saved!")
        save_file.close()
        fs.close()
    if sl == "load":
        save_file = open("login_sheet.txt", "r")
        ld = save_file.read()
        if "\n" in ld:
            load = lister(ld)
        else:
            ln = ld.split()
            if ld != "":
                load = ln
        print("loaded!")
        save_file.close()

save_load("load")
#print(load)

while True:
    try:
        chose_log = input("Do you want to Login[l] or Signup[s] or Quit[q]: ")
        if chose_log[0].lower().strip() == "l":
            chose_log = "login"
        elif chose_log[0].lower().strip() == "s":
            chose_log = "signup"
        elif chose_log[0].lower().strip() == "q" or chose_log[0].lower().strip() == "e":
            chose_log = "quit"
        else:
            int("e")
        break
    except:
        print("Choose a valid option")

def error(nm, err, typ = 0, l_num = 8):
    if typ == 0: #value error
        if err in nm:
            return int("v")
    elif typ == 1: #length error
        if len(nm) < l_num:
            return int("l")
    elif typ == 2: #input error
        if not err in nm:
            return int("v")

def login():
    save_load("load")
    while True:
        try:
            check_list = 0
            usernm = input("Pls write your username here"+
            "(don't add unnesserary symbols): ")
            error(usernm, "@")
            email  = input("Pls write your emailadress "+
            "here(must add a valid email(@gmail.com)): ")
            error(email, "@gmail.com", 2)
            passwd = input("Pls write your password here"+
            "(should be at least" + str(8) +" character): ")
            error(passwd, "", 1)
            for ld in load:
                if ld[1] == usernm:
                    print("usuername correct!")
                    check_list += 1
                    if ld[2] == email:
                        print("email correct!")
                        check_list += 1
                    if ld[3] == passwd:
                        print("password correct!")
                        check_list += 1
            if check_list != 3:
                print("incorrect values!")
            else:
                print("You have Loggedin")
                break
        except ValueError:
            print("Wrong input, Try Again..!")

def signup():
    while True:
        try:
            usernm = str(input("Pls write your username here"+
            "(don't add unnesserary symbols): "))
            error(usernm, "@")
            email  = str(input("Pls write your emailadress "+
            "here(must add a valid email(@gmail.com)): "))
            error(email, "@gmail.com", 2)
            passwd = str(input("Pls write your password here"+
            "(should be at least" + str(8) +" character): "))
            error(passwd, "", 1)
            new_passwd = str(input("Pls write your password again"+
            "to confirm it: "))
            if new_passwd != passwd:
                print("incorrect password!")
                int("m")
            print("You have SignedUp")
            save = "0" + str(len(load)) + ": " + usernm + " " + email + " " + passwd 
            save_load("save", save)
            break
        except:
            print("Wrong input, Try Again..!")
    return save

while True:
    if chose_log == "login":
        print("Welcome to the " + chose_log + " page")
        login()
        break
    elif chose_log == "signup":
        print("Welcome to the " + chose_log + " page")
        signup()
        cont_yn = input("Do you want login now yes[Y] or no[N]: ")
        if cont_yn[0].lower().strip() == "y":
            chose_log = "login"
        else:
            print("Thank you for using the page")
            break
    else:
        break

quit()