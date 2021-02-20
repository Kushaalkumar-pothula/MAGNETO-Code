#Import required libraries
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

time_now = datetime.now().strftime("%Y-%m-%d-%H-%M")

age  = np.loadtxt(time_now+"AgeRes.txt")
flare_intervals = np.loadtxt(time_now+"FlareRes.txt")

#--------------------Plot simulated data-------------------

fig = plt.gcf()
fig.set_size_inches(8,6)

plt.scatter(age, flare_intervals, alpha = 0.8, s = 70, c = flare_intervals, cmap = 'plasma')    #Plot flare intrvals against magnetar age
plt.colorbar()

plt.plot(age,flare_intervals, color ='black', linestyle = ':')    #Line-plot flare intrvals against magnetar age

plt.xlabel("Magnetar Age")
plt.ylabel("Flare Interval")
plt.grid(True)

plt.savefig(time_now+"Flare_Times_Result.png")

#----------------------------------------------------------
