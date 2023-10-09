import matplotlib
import pandas
import seaborn
import numpy

print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

x1 = float(input("Ievadi pieprasījumu: "))
y1 = float(input("Un tam atbilstošo cenu: "))
#print("The entered number is:", x1)
x2 = float(input("Ievadi pieprasījumu: "))
y2 = float(input("Un tam atbilstošo cenu: "))
x3 = float(input("Ievadi piedāvājumu: "))
y3 = float(input("Un tam atbilstošo cenu: "))
#print("The entered number is:", x1)
x4 = float(input("Ievadi piedāvājumu: "))
y4 = float(input("Un tam atbilstošo cenu: "))


b1 = float
b2 = float
k1 = float
k2 = float
def Pieprasijuma_likne(x1, y1, x2, y2):
    k1=(y2-y1)/(x2-x1)
    b1=y1-k1*x1
    return f"y = {k1}x + {b1}"

likne1 = Pieprasijuma_likne(x1, y1, x2, y2)
print("Pieprasījuma līknes vienādojums",likne1)
def Piedavajuma_likne(x3, y3, x4, y4):
    k2=(y4-y3)/(x4-x3)
    b2=y3-k2*x3
    return f"y = {k2}x + {b2}"

likne2 = Piedavajuma_likne(x3, y3, x4, y4)
print("Piedāvājuma liknes vienādojums",likne2)
#xkr = (b2 - b1)/(k1 - k2)
#print("xkrus", xkr)


pieprasijumus1 = np.array([x1, x2])
cena1 = np.array([y1, y2])
piedavajums2 = np.array([x3, x4])
cena2 = np.array([y3, y4])
plt.plot(pieprasijumus1, cena1)
plt.plot(piedavajums2, cena2)
plt.show()
