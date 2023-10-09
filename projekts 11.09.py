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

#float= z    uztaisit taisnes vienadojumu un pagarinat taisni
#print(type(z))
#input(z)

pieprasijumus1 = np.array([x1, x2])
cena1 = np.array([y1, y2])

#jauns

def Pieprasijuma_likne(x1, y1, x2, y2):
k=(y2-y1)/(x2-x1)
b1=y1-k*x1
return f"y = {k}x + {b1}"
likne1 = Pieprasijuma_likne(x1, y1, x2, y2)
print("Pieprasijuma liknes vienadojums", )

piedavajums2 = np.array([10, 7])
cena2 = np.array([0, 250])




plt.plot(pieprasijumus1, cena1)
plt.plot(piedavajums2, cena2)
plt.show()
