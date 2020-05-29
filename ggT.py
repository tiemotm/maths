import math

a = int(input("Erste Zahl: "))
b = int(input("Zweite Zahl: "))

def ggT(a,b):

    while(a != b):

        if(b > a):
            tempA = a
            tempB = b
            b = tempA
            a = tempB

        a = a -b

    print("ggT: " +  str(a))

ggT(a,b)