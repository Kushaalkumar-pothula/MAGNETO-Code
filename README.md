# The Magnetar Activity GeNEraTOr (MAGNETO) Code
An astrophysics based Python code to simulate flaring activity of a magnetar using the Monte Carlo statistical technique. 
The MAGNETO code generates a sequence of flares from a single magnetar over its lifetime. Remember that the Monte Carlo simulation has been performed for a linear relation ONLY. This will be updated based on the astrophysics and physics of magnetars soon.


## Installation

To install the MAGNETO code, run the following commands in the terminal:
```bash
mkdir MAGNETO-Code
cd MAGNETO-Code
git clone https://github.com/Kushaalkumar-pothula/MAGNETO-Code.git
cd MAGNETO-Code
```
Now you should have the MAGNETO code successfully installed on your computer. Now you can proceed to running the code using the commands described in the section below.

## Usage
To run the code, you must have NumPy and Matplotlib already installed.

#### UNIX Operating Systems
You can run and analyse the simulation in a single step by running ```run.sh```. This can be done by running the following commands in a terminal:
```bash
chmod +x run.sh
./run.sh
```

#### Windows and Others OS
Run the following command:
```bash
python FlareTimes.py
```
This command  will result in a simulation of flare intervals of flaring activity of a magnetar.

Now, you can analyse the result obtained by running the Monte Carlo simulation by running the command:
```bash
python FlareTimePlot.py
```
This command will result in a plot showing the simulated relation of the age of a magnetar and its flare intervals.

## Results
The results are availabe as ```AgeRes.txt``` and ```FlareRes.txt```. These files denote the results of magnetar age and flare intervals respectively. *Do not* rename these files!

You will also find a file ```Flare_Times_Result.png``` in the ```MAGNETO-Code``` directory. This plot displays the relation between flaring activity of the magnetar over its lifetime. Remember to copy this plot to another directory for later use, or else it will be replaced when you run the code again. 
