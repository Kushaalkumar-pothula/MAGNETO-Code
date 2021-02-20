#!/bin/sh
echo "Starting MAGNETO"

echo "Initialising simulation"
python FlareTimes.py
echo "Simulation complete"

echo "Initialising analysis"
python FlareTimePlot.py
echo "Analysis complete"
