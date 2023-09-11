import matplotlib

print(matplotlib.__version__)


import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([0, 6, 20])
ypoints = np.array([0, 250, 300])


plt.plot(xpoints, ypoints)
plt.show()