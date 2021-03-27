# Import required libraries
import numpy as np


year = 3.15e7
t0 = year / 12.0
t = t0
flare_times = [t]


def flaring_rate(t):
    return 1e-6 * (t / t0)**-1.0


def interval_gen(lst_a,lst_f):
    year = 3.15e7
    t0 = year / 12.0
    t = t0
    while t < 1000.0 * year:
        lst_a.append(t)
        t += np.random.exponential(scale=1.0 / flaring_rate(t))
        lst_f.append(t)
