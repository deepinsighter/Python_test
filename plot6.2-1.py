import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

fig = plt.figure()

x = np.linspace(0.0,2*np.pi)  # num=50
y = np.cos(x) * np.sin(x)

ax1 = fig.add_subplot(1,2,1)
ax1.margins(0.03)                      
ax1.plot(x, y, ls='-', lw=2, color='b')

ax2 = fig.add_subplot(2,2,2)
ax2.margins(0.5, 0.7)
ax2.plot(x, y, ls='-', lw=2, color='r')

ax3 = fig.add_subplot(2,2,4)
ax3.margins(x=0.1,y=0.3)
ax3.plot(x, y, ls='-',lw=2,color='g')

plt.show()
