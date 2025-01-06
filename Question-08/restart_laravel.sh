#!/bin/bash

# Variables
SERVICE_NAME="laravel-backend"  # Replace with your Laravel service name
CPU_THRESHOLD=80
LOG_FILE="/var/log/restart_laravel.log"

# Function to get current CPU usage
get_cpu_usage() {
  # Uses 'top' command to extract CPU usage
  CPU=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
  echo "$CPU"
}

# Function to restart Laravel service
restart_service() {
  echo "$(date): CPU usage is $CPU%, restarting $SERVICE_NAME" >> $LOG_FILE
  systemctl restart $SERVICE_NAME
  if [ $? -eq 0 ]; then
    echo "$(date): $SERVICE_NAME restarted successfully" >> $LOG_FILE
  else
    echo "$(date): Failed to restart $SERVICE_NAME" >> $LOG_FILE
  fi
}

# Main monitoring loop
while true; do
  CPU=$(get_cpu_usage)
  CPU_INT=${CPU%.*}  # Convert CPU usage to an integer for comparison

  if [ "$CPU_INT" -gt "$CPU_THRESHOLD" ]; then
    restart_service
  fi

  # Sleep for a minute before the next check
  sleep 60
done
