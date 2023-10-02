import matplotlib
import pandas
import seaborn
import numpy

print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

pieprasijumus1 = np.array([0, 7, 20])
cena1 = np.array([0, 250, 300])

piedavajums2 = np.array([10, 7, 20])
cena2 = np.array([0, 250, 300])




plt.plot(pieprasijumus1, cena1)
plt.plot(piedavajums2, cena2)
plt.show()
