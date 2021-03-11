#!/bin/sh

echo "
___  ___  ___  _____  _   _  _____ _____ _____ 
|  \/  | / _ \|  __ \| \ | ||  ___|_   _|  _  |
| .  . |/ /_\ \ |  \/|  \| || |__   | | | | | |
| |\/| ||  _  | | __ | . ` ||  __|  | | | | | |
| |  | || | | | |_\ \| |\  || |___  | | \ \_/ /
\_|  |_/\_| |_/\____/\_| \_/\____/  \_/  \___/ " 
                                               
                                               
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

elapsed="$(($end_time-$start_time))"
echo "MAGNETO simulation completed successfully in $elapsed seconds."
