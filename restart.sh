#!/bin/bash

# Define the name of the Flask app and the command to start it
app_name="app.py"
start_command="python $app_name"

# Define the PID file
pid_file="app.pid"

# Check if the PID file exists
if [ -f "$pid_file" ]; then
  pid=$(cat "$pid_file")
  if ps -p "$pid" > /dev/null; then
    echo "Flask app is already running with PID $pid."
    exit 0
  else
    echo "Stale PID file found. Removing..."
    rm "$pid_file"
  fi
fi

# If the PID file doesn't exist or the process is not running, start the app
echo "Starting Flask app..."
$start_command &
# Capture the PID of the newly started process
echo $! > "$pid_file"
echo "Flask app started with PID $!"
