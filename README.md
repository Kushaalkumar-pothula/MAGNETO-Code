# The Magnetar Activity GeNEraTOr (MAGNETO) Code

[![DOI](https://zenodo.org/badge/340451011.svg)](https://zenodo.org/badge/latestdoi/340451011)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


An astrophysics based Python code to simulate flaring activity of a magnetar using the Monte Carlo statistical technique. 
The MAGNETO code generates a sequence of flares from a single magnetar over its lifetime to determine how the time between two flares and flare energies evolve over the magnetar's age.


## Installation

To install the MAGNETO code, run the following commands in a terminal:
```bash
> git clone https://github.com/Kushaalkumar-pothula/MAGNETO-Code.git
> cd MAGNETO-Code
```
Now you should have the MAGNETO code successfully installed on your computer. Now you can proceed to run the code.

## Usage
*Dependencies*: Python 3, NumPy and Matplotlib. 
There are two ways to run MAGNETO: By following the default method or the custom method. The custom method gives more freedom over physical parameters.

### Default Configuration
1. Open MAGNETO-Code directory in your terminal.
2. Run the following command:
```bash
> bash run.sh
```
This will run the simulation with some default values of the magnetar's magntic field energy and power-law index.

### Custom Configuration
In this method of running MAGNETO, you will have control over the physical aspects of the magnetar. You can specify the values of the respective parameters using options while running scripts. To get help with them, you can use the ```-h``` flag while running the script:
```bash
> python energy_evol_modular.py -h
  usage: energy_evol_modular.py [-h] E [E ...] a [a ...]

Simulate flaring activity of a magnetar using the Monte Carlo method.

positional arguments:
  E           Total magetic energy of the magnetar
  a           Power of time in energy-time relation, known as alpha

optional arguments:
  -h, --help  show this help message and exit
```
  
## Author
Kushaal Kumar Pothula (www.sites.google.com/view/kushaal-kumar-pothula)
