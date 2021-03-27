# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
from interval_module import interval_gen

lst_a = [] 
lst_f = []
interval_gen(lst_a, lst_f)
#--------------------Plot simulated data-------------------

fig = plt.gcf()
fig.set_size_inches(8, 6)

# Plot flare intrvals against magnetar age
plt.scatter(lst_a, lst_f, alpha=0.8, s=70, c=lst_f, cmap='plasma')
plt.colorbar()
# Line-lot flare intrvals against magnetar age
#plt.plot(lst_a, lst_f, color='black', linestyle=':')
plt.xlabel("Magnetar Age [seconds]")
plt.ylabel("Flare Interval [seconds]")
plt.grid(True)
plt.show()

#----------------------------------------------------------
