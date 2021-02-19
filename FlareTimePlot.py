#Import required libraries
import numpy as np
import matplotlib.pyplot as plt

age  = np.loadtxt("AgeRes.txt")
flare_intervals = np.loadtxt("FlareRes.txt")

#--------------------Plot simulated data-------------------

fig = plt.gcf()
fig.set_size_inches(8,6)

plt.scatter(age, flare_intervals, alpha = 0.8, s = 70, c = flare_intervals, cmap = 'plasma')    #Plot flare intrvals against magnetar age
plt.colorbar()

plt.plot(age,flare_intervals, color ='black', linestyle = ':')    #Line-lot flare intrvals against magnetar age

plt.xlabel("Magnetar Age")
plt.ylabel("Flare Interval")
plt.grid(True)

#----------------------------------------------------------