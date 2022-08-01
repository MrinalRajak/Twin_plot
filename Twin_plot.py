

#Twin plot using matplotlib

import numpy as np
import matplotlib.pyplot as plt
T=np.linspace(0,5,200)
V=10*(1-np.exp(-T))
I=np.exp(-T)

plt.rcParams.update({'font.size':15,'lines.linewidth':2})
fig,ax1=plt.subplots()
ax2=ax1.twinx()
ax1.plot(T,V,color='r')
ax2.plot(T,I,color='m')
ax1.set_xlabel('Time',color='green')
ax1.set_ylabel('Voltage',color='chocolate')
ax2.set_ylabel('Current',color='blue')
plt.show()
