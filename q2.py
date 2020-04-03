import math

a = (input(" ax2 + bx + c = d Geben Sie den Koeffizient der ersten Gleichung a an:"))
b = (input(" ax2 + bx + c = d Geben Sie den Koeffizient der ersten Gleichung b an:"))
c = (input(" ax2 + bx + c = d Geben Sie den Koeffizient der ersten Gleichung c an:"))

def loese(a, b, c):
    
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

loese(a, b, c)