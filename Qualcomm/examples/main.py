import numpy as np
import scipy as sp
from load import load_data
drivers, pins= load_data()
import matplotlib.pyplot as plt 
import numpy as np
plt.scatter(drivers['x'], drivers['y'])
plt.scatter(pins['x'],pins['y'])
plt.show()