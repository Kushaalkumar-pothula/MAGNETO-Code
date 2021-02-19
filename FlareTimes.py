#Import required libraries
import numpy as np

#--------------------Monte Carlo Simmulation---------------

lst_f = []  #List to hold flare intervals
lst_a = []  #List to hold magnetar age

year = 3.15e7
t0 = year / 12.0
t = t0
flare_times = [t]
 
def flaring_rate(t):
      return 1e-6 * (t / t0)**-1.0

t_pre = np.random.exponential(1)    #Initial flaring interval

while t < 1000.0 * year:
    lst_a.append(t)
    t += np.random.exponential(scale=1.0 / flaring_rate(t))
    lst_f.append(t)
    
  
arr_f = np.array(lst_f)
arr_a = np.array(lst_a)

np.savetxt("Flare Interval Result.txt",arr_f)
np.savetxt("Magnetar Age.txt",arr_a)

#----------------------------------------------------------