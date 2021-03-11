#!/bin/sh
  
                                               
current_date_time="`date "+%Y-%m-%d %H:%M"`";
echo "Starting MAGNETO at $current_date_time"


echo "Starting MAGNETO..."
start_time="$(date -u +%s)"

echo "Starting flaring interval simulation..."
python FlareTimes.py
python FlareTimePlot.py &
echo "Starting energy evolution simulation..."
python energyevol.py &
wait
echo "Done"
end_time="$(date -u +%s)"
elapsed="$(($end_time-$start_time))"
echo "MAGNETO simulation completed successfully in $elapsed seconds."
