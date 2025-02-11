import time
import re
import logging
import json
import os
from collections import defaultdict

# Global configuration variables (will be set by load_config)
LOG_FILE = ""
ALERT_LOG_FILE = ""
ALERT_THRESHOLD = 0
CHECK_INTERVAL = 0

# Dictionary to track failed login attempts per IP
login_attempts = defaultdict(int)

# Determine configuration file path (assumes config is in ../config/config.json relative to src)
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../config/config.json")

def load_config(config_path=CONFIG_PATH):
    """
    Load configuration from a JSON file and set global variables.
    """
    global LOG_FILE, ALERT_LOG_FILE, ALERT_THRESHOLD, CHECK_INTERVAL

    try:
        with open(config_path, "r") as f:
            config = json.load(f)
        LOG_FILE = config["log_file"]
        ALERT_LOG_FILE = config["alert_log_file"]
        ALERT_THRESHOLD = config["alert_threshold"]
        CHECK_INTERVAL = config["check_interval"]

        if not all([LOG_FILE, ALERT_LOG_FILE, ALERT_THRESHOLD, CHECK_INTERVAL]):
            raise ValueError("One or more required configuration fields are missing.")

        print(f"Configuration loaded: {LOG_FILE}, {ALERT_LOG_FILE}, {ALERT_THRESHOLD}, {CHECK_INTERVAL}")
    except Exception as e:
        print(f"Error loading configuration: {e}")
        exit(1)

def setup_logging():
    """
    Set up logging configuration to write alerts to the alert log file.
    """
    # Ensure the directory for ALERT_LOG_FILE exists
    log_dir = os.path.dirname(ALERT_LOG_FILE)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Ensure the directory for LOG_FILE exists (if not, create it)
    log_dir = os.path.dirname(LOG_FILE)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logging.basicConfig(
        filename=ALERT_LOG_FILE,
        level=logging.WARNING,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    print(f"Logging is set up and writing to {ALERT_LOG_FILE}")

def process_log_entry(entry):
    """
    Process a single log entry.
    If the entry indicates a failed login attempt, update the count for that IP.
    If the count is at least ALERT_THRESHOLD, log an alert to alert_log.txt.
    """
    global login_attempts
    failed_login_pattern = r"Failed login attempt from (\S+)"
    match = re.search(failed_login_pattern, entry)
    if match:
        ip_address = match.group(1)
        login_attempts[ip_address] += 1
        current_count = login_attempts[ip_address]

        # If the failed attempts reach the threshold, create an alert message
        if current_count >= ALERT_THRESHOLD:
            # Create alert message in desired format
            alert_message = f"[ALERT]{current_count} failed logins from {ip_address} ({current_count} attempts)"
            
            # Write the alert message into alert_log.txt
            logging.warning(alert_message)

            # Optionally print the alert message to the terminal, overwrite with \r
            print(f"\r{alert_message}", end="", flush=True)

def tail_log_file():
    """
    Continuously monitor the log file for new lines.
    Only processes lines that are added after the current end of file.
    """
    with open(LOG_FILE, "r") as file:
        file.seek(0, os.SEEK_END)  # Move to the end of the file
        while True:
            line = file.readline()
            if line:
                process_log_entry(line)
            else:
                time.sleep(CHECK_INTERVAL)

def process_existing_logs():
    """
    Process all existing log lines (so that previously written lines are counted).
    """
    with open(LOG_FILE, "r") as file:
        for line in file:
            process_log_entry(line)

if __name__ == "__main__":
    load_config()
    setup_logging()
    # First, process any existing logs
    process_existing_logs()
    # Then, start real-time monitoring of new log entries
    tail_log_file()
