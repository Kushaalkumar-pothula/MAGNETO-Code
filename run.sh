#!/bin/sh

echo "Starting MAGNETO at:"
current_date_time="`date "+%Y-%m-%d %H:%M"`";
echo $current_date_time;

echo "Initializing simulation"
python FlareTimes.py
echo "Simulation complete"

echo "Initializing analysis"
python FlareTimePlot.py
echo "Analysis complete"
