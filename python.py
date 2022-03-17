    #Returns the sum of numb1 and numb2
def add(numb1, numb2):
    return numb1 + numb2

def sub(numb1, numb2):
    return numb1 - numb2

def mult(numb1, numb2):
    return numb1 * numb2

def div(numb1, numb2):
    return numb1 / numb2

def main():
    operation = input("What do you want to do (+,/,*,-)")
    if operation == "+" or operation == "-" or operation == "/" or operation == "*":
        numb1 = int(input("Enter numb1: "))
        numb2 = int(input("Enter numb2: "))
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
            sum = div(numb1, numb2)
            print(sum)
    else:
        print("Enter a valid operation")

myList = [2,8]
sum = add(*myList) #new expreiment with this feature => try loops make this code better
print(sum)

main()