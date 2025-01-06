
# Question 08: 
Restart Laravel Backend Service if CPU Usage Exceeds 80%

## Problem Statement

High CPU usage can degrade the performance of the Laravel backend service. In a VM-based deployment, monitoring CPU usage and restarting the service automatically when usage exceeds a defined threshold (e.g., 80%)

---

## Solution

The provided shell script monitors CPU usage and restarts the Laravel backend service if the usage exceeds the threshold. It logs all actions for auditability and runs continuously in the background.

---

## Instructions



### 1. Set Permissions
- Make the script executable:
  ```bash
  chmod +x restart_laravel.sh
  ```

### 3. Run the Script
- Execute the script manually:
  ```bash
  /restart_laravel.sh &
  ```

### 4. Automate Execution
- Add the script to `crontab` for periodic execution:
  ```bash
  crontab -e
  ```
- Add the following line to check every minute:
  ```bash
  * * * * * /restart_laravel.sh
  ```

---

## Script Features

1. **CPU Monitoring**:
   - The script uses the `top` command to monitor CPU usage and extracts the overall CPU utilization.

2. **Service Restart**:
   - If CPU usage exceeds the threshold, the Laravel service is restarted using `systemctl`.

3. **Logging**:
   - All actions, including CPU usage and service restart events, are logged to `/var/log/restart_laravel.log`.

---