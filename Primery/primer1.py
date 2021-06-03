import math
x=float(input("Vvedite x:"))
if x<=0:
    y=2*x*x+math.cos(x)
elif x<5:
    y=x+1
else:
    y=math.sin(x)-x*x
print('Y raven:', "%.2f"%y)