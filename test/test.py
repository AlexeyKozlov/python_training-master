
from math import sqrt

def qawadrat(a,b,c):
    d = b*b - 4*a*c
    if d < 0:
        print("Net recshenia")
    elif d == 0:
            x = -b / (2*a)
            print("Odno rechenie "+"x1= "+str(x)+" and x2= "+str(x))
    elif d > 0:
        x1 = (-b-sqrt(d)) / (2*a)
        x2 = (-b+sqrt(d)) / (2*a)
        print("Dva rechenia "+"x1= "+str(x1)+" and x2= "+str(x2))
    else:
       print("A-A-A-A!")

qawadrat(1,1,1)
qawadrat(1,2,1)
qawadrat(1,5,6)