import math

a = int(input(" a*x2 + b*x + c = d Type the first(a) coefficient in :"))
b = int(input(" a*x2 + b*x + c = d Type the second(b) coefficient in:"))
c = int(input(" a*x2 + b*x + c = d Type the third(c) coefficient in:"))
d = int(input(" a*x2 + b*x + c = d Type the fourth(d) coefficient in:"))

def solve(a, b, c, d):
    
    if(a == 1 and d == 0):
        try:
            sq = (((b/2)**2 - c))
            sqrt = math.sqrt(sq)

            x1 = (-(b/2) + sqrt)
            x2 = (-(b/2) - sqrt)

            if(x1 == x2):
                print("x =",x1)
            else:
                print("x1 =",x1,", x2 =",x2)
        except:
            print("No Solution")
    else:
        aOld = a
        a = a/aOld
        b = b/aOld
        c = c/aOld

        d = d/aOld
        c = c - d
        d = d - d
        solve(a, b, c, d)

solve(a, b, c, d)