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
This command will run a Monte Carlo simulation of flaring activity of a magnetar. The results are availabe as ```AgeRes.txt``` and ```FlareRes.txt```. *Do not* rename these files!

Now, you can analyse the results obtained by running the Monte Carlo simulation by running the command:
```bash
python FlareTimePlot.py
```
You should now find a file ```Flare_Times_Result.png``` in the ```MAGNETO-Code``` directory. This plot displays the relation between flaring activity of the magnetar over its lifetime. Remember to copy this plot to another directory for later use, or it will be replaced when you run the code again. 

Remember that the Monte Carlo simulation has been performed for a linear relation ONLY. This will be updated based on the astrophysics and physics of magnetars soon.

## Shell Script for Simulation
You can skip the above steps by running ```run.sh```, which combines both the simulation and analysis steps, by following the instructions below. But this works only on UNIX operating systems:
```bash
chmod +x run.sh
./run.sh
```
```run.sh``` just combines of the commands mentioned in the "Usage" section.

