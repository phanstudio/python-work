def _error(type, check):
    message = ""
    numericals = [0,1,2,3,4,5,6,7,8,9]
    if type == "space":
        if " " in check:
            message = "Pls remove all spaces, try again"
    if type == "numerical":
        for num in numericals:
            if str(num) in check:
                message = "Pls remove all the numbers, try again"
                break
    if type == "numb":
        try:
            int(check)
        except:
            message = "Pls only write numbers"
    return message

def i_error(type, check):
    """
    This handles errors 
    """
    message = ""
    if type == "space" or type == 0:
        for i in check:
            if i.isspace(): message = "Pls remove all spaces, try again" ; break
    if type == "numerical" or type == 1:
        for i in check:
            if i.isnumeric(): message = "Pls remove all the numbers, try again" ; break
    if type == "numb" or type == 2:
        try: int(check)
        except: message = "Pls only write numbers"
    if type == 3:
        pass
    return message

class DialogReader:
    def __init__(self) -> None:
        pass
    @staticmethod
    def dialog(txt:str= "", error_type = [], validation:str= "", quiter:bool= True):
        """
        => txt:\n
        => error type: (0-3) space(0): An error will occur if there is a space in the string; numerical(1): An error if any number is found in the string; numb(2): An error will not occur if only number are in the string\n
        eg. if txt= "1sen#" and error_type= 2; An error will occur\n
        => validation: If you want to show a message after the code ran\n
        => quiter: if true and the quit icon will show ;else it won't
        """
        if quiter == True:
            log = "(Quit): "
        else:
            log = ": "
        while True:
            try:
                ask = input(txt + log)
                error_message = []
                for error in error_type:
                    error_message.append(_error(error, ask))
                    if "" in error_message:
                        error_message.clear()
                if error_message:
                    int("e")
                if ask.lower() == "quit":
                    quit()
                if validation:
                    print(validation + "!")
                break
            except:
                for error in error_message:
                    if error:
                        print(str(error) + "!")
                if ask.lower() == "quit":
                    quit()
        return ask

def cor(num, v:int= 3):
    """
    => Num: Type a number in num and it converts it to a human readable format\n
    eg. if num = 100000: => 100K\n
    => V or Value: Divider(Control the amount before it breaks it)
    """
    li_of_val, b = ["", "k", "m", "b", "t", "q", "qi"], 0 # assigning variables
    while True:
        y = num / 10**(v * b)
        if y < 10**v: break
        b += 1
    return str(round(num / 10**(v * b), 2)) + li_of_val[(b)].capitalize()

"""DialogReader.dialog("input any letter no numbers and spaces",["numerical", "space"])
DialogReader.dialog("input any letter no numbers",["numerical"], "works")
DialogReader.dialog("input any number",["numb"], "works")
cor(99908908000000000)"""