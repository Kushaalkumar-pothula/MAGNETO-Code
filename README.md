# The Magnetar Activity GeNEraTOr (MAGNETO) Code
An astrophysics based Python code to simulate flaring activity of a magnetar using the Monte Carlo statistical technique. 
The MAGNETO code generates a sequence of flares from a single magnetar over its lifetime. Remember that the Monte Carlo simulation has been performed for a linear relation ONLY. This will be updated based on the astrophysics and physics of magnetars soon.


## Installation

To install the MAGNETO code, run the following commands in a terminal:
```bash
> mkdir MAGNETO-Code
> cd MAGNETO-Code
> git clone https://github.com/Kushaalkumar-pothula/MAGNETO-Code.git
> cd MAGNETO-Code
```
Now you should have the MAGNETO code successfully installed on your computer. Now you can proceed to running the code using the commands described in the section below.

## Usage
To run the code, you must have NumPy and Matplotlib already installed. 
If you have fulfilled the requirements, you can proceed to run the code.

In a ```bash``` shell, you can run and analyse the simulation in a single step by running ```run.sh```. This can be done by running the following commands in a terminal:
```bash
> chmod +x run.sh
> ./run.sh
```

If you want to run individual scripts, you can follow the instructions below:
Run the following command:
```bash
> python FlareTimes.py
```
This command  will run a simulation of flare intervals of flaring activity of a magnetar.

Now, you can analyse the result obtained by running the Monte Carlo simulation by running the command:
```bash
> python FlareTimePlot.py
```
This command will result in a plot showing the simulated relation of the age of a magnetar and its flare intervals.

## Results
The results are availabe as ```.txt``` files, which are named as ```[date-time]AgeRes.txt``` and ```[date-time]FlareRes.txt``` where ```date-time``` is replaced by your local time from your computer. These files denote the results of magnetar age and flare intervals respectively. Because the analysis script (```FlareTimePlot.py```) reads the output of the simulation script (```FlareTimes.py```), *do not* rename these outputs and give at least a 1 minute gap between two consequtive runs of MAGNETO.
You will find a file ```[date-time]Flare_Times_Result.png``` in the ```MAGNETO-Code``` directory. This plot, an output of the analysis script, displays the relation between flaring activity of the magnetar over its lifetime.

## Author
Kushaal Kumar Pothula (www.sites.google.com/view/kushaal-kumar-pothula)
