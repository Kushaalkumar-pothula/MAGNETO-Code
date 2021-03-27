# Import required libraries
import os
from datetime import datetime

from interval_module import interval_gen
import matplotlib.pyplot as plt

lst_a = [] 
lst_f = []
interval_gen(lst_a, lst_f)

fig = plt.gcf()
fig.set_size_inches(8, 6)
plt.scatter(lst_a, lst_f, alpha=0.8, s=70, c='r')
plt.xlabel("Magnetar Age [seconds]")
plt.ylabel("Flare Interval [seconds]")
plt.grid(True)

time_now = datetime.now().strftime('%d-%m-%Y-%H-%M')
plt.savefig(f'{time_now}_flare_interval_evolution.png')
