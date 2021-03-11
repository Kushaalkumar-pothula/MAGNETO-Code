import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

time_now = datetime.now().strftime("%Y-%m-%d-%H-%M")
flare_interval = np.loadtxt(time_now+"FlareRes.txt")
age = np.loadtxt(time_now+"AgeRes.txt")

lst_edot = []  # Empty list to hold E-dot values

for a in age:
    # E-dot is proportional to t^-alpha where alpha = 1.3
    edot = (1e46 * (a**(-1.3)))  # 1e46 because it is roughly E_B of SGR 1935
    lst_edot.append(edot)


lst_e = []


def energy_calc(edot, t_int):
    """
    Calculates magnetar giant flare energy for a given flare interval,
    based on the energy injection rate and a flare interval (directly
    from the magnetar's age).

    Args:
    - edot: Energy injection rate at a specific age
    - t_int: Flare interval at a given age

    Returns:
    - e_f: Flare energy for a given E-dot and flare interval at a specific
     age
    """
    e_f = edot * t_int  # As E-dot is defined as e_f/t_int
    return e_f
#--------------------------------------------------------------------------


e = list(map(energy_calc, lst_edot, flare_interval))

arr_e = np.array(e)

plt.scatter(lst_a, arr_e, s=36, alpha=2, c=arr_e, cmap="plasma")
plt.clim(0.3e44, 1.5e44)
plt.colorbar(extend='both')
#plt.plot(lst_a, arr_e, linestyle=":", color='black')

plt.xlabel("Magnetar Age [seconds]")
plt.ylabel("Flare Energy [ergs]")
plt.grid(True)

plt.savefig(time_now+"energy_evolution.png")
