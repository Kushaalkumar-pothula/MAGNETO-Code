# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
from interval_module import interval_gen

lst_a = [] 
lst_f = []
interval_gen(lst_a, lst_f)

fig = plt.gcf()
fig.set_size_inches(8, 6)
# Plot flare intrvals against magnetar age
plt.scatter(lst_a, lst_f, alpha=0.8, s=70, c='r')
plt.xlabel("Magnetar Age [seconds]")
plt.ylabel("Flare Interval [seconds]")
plt.grid(True)
#Save plot
plt.savefig(f'{dirname}/flare_interval_evolution.png')
