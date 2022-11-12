import numpy as np
import scipy as sp
from load import load_data
drivers, pins= load_data()
import matplotlib.pyplot as plt 
import numpy as np
print(drivers.max(), drivers.min())
print(pins.max(), pins.min())
plt.scatter(drivers.loc[drivers['input_output']=='INPUT',['x']], drivers.loc[drivers['input_output']=='INPUT',['y']],label='input')
plt.scatter(drivers.loc[drivers['input_output']=='OUTPUT',['x']], drivers.loc[drivers['input_output']=='OUTPUT',['y']],label='output')
plt.scatter(pins['x'],pins['y'])
plt.legend()
plt.show()