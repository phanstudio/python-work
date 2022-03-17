import math

def almity(a:int, b:int, c:int):
    """
    in an quad equation \n
    (4x^2 =a), (-11x =b), (-21 =c) => a= +4, b= -11, c= -21 \n
    x,y = (-b +- sqrt(b^2 -4ac))/ 2a \n
    it returns 2 anwsers which are +x and (-x or y)
    """
    x =  round(math.sqrt(((b**2)  - (4*a*c))), 3)
    y = (round((-b + x)/(2*a), 2),round((-b - x)/(2*a), 2))
    print("(x= " + str(y[0]) + ", y= " + str(y[1]) + ")")
    return y

# y = 4x^2 -11x -21
almity(400,-1100,-21)