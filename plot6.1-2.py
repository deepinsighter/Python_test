import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rcParams["font.sans-serif"] = ["FangSong"]
mpl.rcParams["axes.unicode_minus"] = False

radii = np.linspace(0,1,100)
theta = 3*np.pi*radii

ax = plt.subplot(1,1,1, polar=True)
ax.plot(theta,radii,color='r',linestyle='-',linewidth=2)

plt.show()