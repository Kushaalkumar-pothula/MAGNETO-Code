# The MAGNETO Code: Magnetar Activity GeNEraTOr
An astrophysics based Python code to simulate flaring activity of a magnetar using the Monte Carlo statistical technique.

## Installation
To install this code, run the following commands in the terminal:
```bash
mkdir MAGNETO-Code
cd MAGNETO-Code
git clone https://github.com/Kushaalkumar-pothula/MAGNETO-Code.git
cd MAGNETO-Code
```
Now you should have the MAGNETO code successfully installed on your computer

## Usage
To run the code, you must have NumPy and Matplotlib already installed.
Now, in the terminal where you had ran the previous commands, run the following command:
```bash
python FlareTimes.py
```
This command will run a Monte Carlo simulation of flaring activity of a magnetar. The results are availabe as ```AgeRes.txt``` and ```FlareRes.txt```. Do NOT rename these files!
Now, you can plot the results obtained by running the Monte Carlo simulation by running the command:
```bash
python FlareTimePlotpy
```
Now you should find a file ```Flare_Times_Result.png```. This plot displays the relation between flaring activity of the magnetar over its lifetime.
Remember that the Monte Carlo simulation has been performed for a linear relation ONLY. This will be updated based on the astrophysics and physics of magnetars soon.
