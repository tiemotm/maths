import math

a = (input(" ax2 + bx + c = d Type the first(a) coefficient in :"))
b = (input(" ax2 + bx + c = d Type the second(b) coefficient in:"))
c = (input(" ax2 + bx + c = d Type the third(c) coefficient in:"))

def solve(a, b, c):
    
    if(a == 1):
        try:
            sq = (((b/2)**2 - c))
            sqrt = math.sqrt(sq)

            x1 = (-(b/2) + sqrt)
            x2 = (-(b/2) - sqrt)

            print("x1 =",x1,", x2 =",x2)
        except:
            print("Keine Lösung")
    else:
        x = 1/a

solve(a, b, c)