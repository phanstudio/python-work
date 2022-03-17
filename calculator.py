from collections import namedtuple
print("Calculator")
calculate = input(": ")
calculate = "5+5+5/9+6+9/5"
operation = True
while operation:
    num1 = ""
    num2 = ""
    operate = ""
    n = 0
    length = 0
    j = 1
    t = 1
    b = 0
    a = 0
    #arrange the numbers
    for i in range(len(calculate)):
        if calculate[i] == "/":
            while (b != 1 and a != 1):
                if i - (j + 1) != -1 and (calculate[i - (j + 1)] != "+"):
                    j += 1
                else:
                    b = 1
                if i + (t + 1) < len(calculate) and (calculate[i + (t + 1)] != "+"):
                    t += 1
                else:
                    a = 1
            if calculate[i - (j + 1)] == "+":
                calculate = calculate[i - (j):i + (t + 1)] + calculate[i - (j + 1)] + calculate[:i - (j + 1)] + calculate[i + (t + 1):]
            elif i - (j + 1) == -1:
                pass
            break

    for i in calculate:
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
    
    calculate = calculate[length:]
    if calculate == "":
        operation = False

    #Returns the sum of numb1 and numb2
    if True:
        def add(x, y):
            return x + y

        def sub(x, y):
            return x - y

        def mult(x, y):
            return x * y

        def div(x, y):
            return x / y

    def main():
        operation = operate
        if operation == "+" or operation == "-" or operation == "/" or operation == "*":
            numb1 = int(num1)
            numb2 = int(num2)
            if operation == "+":
                sum = add(numb1, numb2)
                print(sum)
            elif operation == "-":
                sum = sub(numb1, numb2)
                print(sum)
            elif operation == "*":
                sum = mult(numb1, numb2)
                print(sum)
            elif operation == "/":
                sum = round(div(numb1, numb2))
                print(sum)
        return str(sum) + "" + calculate

    calculate = main()
    if operation == False:
        break