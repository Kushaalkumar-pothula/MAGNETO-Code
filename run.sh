#!/bin/sh

current_date_time="`date "+%Y-%m-%d %H:%M"`";
echo "Starting MAGNETO at $current_date_time"


echo "Initializing simulation..."
start_time="$(date -u +%s)"

python FlareTimes.py
echo "Simulation complete"

echo "Initializing analysis..."
python FlareTimePlot.py

end_time="$(date -u +%s)"
echo "Analysis complete"


elapsed="$(($end_time-$start_time))"
echo "MAGNETO simulation completed successfully in $elapsed seconds."
