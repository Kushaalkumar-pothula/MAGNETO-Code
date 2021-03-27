
import argparse

from interval_module import interval_gen
import matplotlib.pyplot as plt

#-----------------------Argument Parser----------------------------------
parser = argparse.ArgumentParser(
    description='Simulate flaring activity of a magnetar using the Monte Carlo method.')
parser.add_argument('energy', metavar='E', type=float, nargs='+',
                    help='Total magetic energy of the magnetar')
parser.add_argument('alpha', metavar='a', type=float, nargs='+',
                    help='Power of time in energy-time relation, known as alpha')

args = parser.parse_args()
e_b = args.energy[0]
alp = args.alpha[0]
#------------------------------------------------------------------------
lst_f = []  # List to hold flare intervals
lst_a = []  # List to hold magnetar age

interval_gen(lst_a, lst_f)

#-----------------------Energy injection rate-----------------------------

lst_edot = []  # Empty list to hold E-dot values

for a in lst_a:
    # E-dot is proportional to t^-alpha where alpha = 1.3
    edot = (e_b * (a**(-(alp))))  # 1e46 because it is roughly E_B of SGR 1935
    lst_edot.append(edot)

#-------------------------------------------------------------------------


#----------------------Flare Energy Evolution-----------------------------
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


e = list(map(energy_calc, lst_edot, lst_f))

plt.scatter(lst_a, e, s=36, alpha=2, c=e, cmap="plasma")
plt.colorbar()
plt.xlabel("Magnetar Age [seconds]")
plt.ylabel("Flare Energy [ergs]")
plt.grid(True)
plt.savefig(f'{dirname}/enrgy_evolution.png')
