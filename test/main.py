import matplotlib.pyplot as plt
import numpy as np

d = np.loadtxt('WDs_Tremblay+2017.dat')
   

x_data = d[:,0]
y_data = d[:,1]

plt.scatter(x_data, y_data)
plt.show()