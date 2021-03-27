#!/bin/sh
  
                                               
current_date_time="`date "+%Y-%m-%d %H:%M"`";
echo "Starting MAGNETO at $current_date_time"

start_time="$(date -u +%s)"

echo "Starting simulation..."
python interval_evol_modular.py &
python energy_evol_modular.py 1e46 1.3 &
wait
end_time="$(date -u +%s)"
elapsed="$(($end_time-$start_time))"
echo "MAGNETO simulation completed successfully in $elapsed seconds."
