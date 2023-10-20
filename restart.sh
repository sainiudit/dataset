#!/bin/bash

# Define the name of the Flask app and the command to start it
app_name="app.py"
start_command="python $app_name"

# Check if the app is already running
if ps aux | grep -v "grep" | grep "$app_name" > /dev/null; then
  echo "Flask app is already running."
else
  # If not running, start the app
  echo "Starting Flask app..."
  $start_command &
  echo "Flask app started."
fi
