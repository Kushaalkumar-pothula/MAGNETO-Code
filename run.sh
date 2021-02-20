#!/bin/sh

echo "Starting MAGNETO at:"
current_date_time="`date "+%Y-%m-%d %H:%M"`";
echo $current_date_time;

echo "Initialising simulation"
python FlareTimes.py
echo "Simulation complete"

echo "Initialising analysis"
python FlareTimePlot.py
echo "Analysis complete"
