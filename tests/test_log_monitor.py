import json
import os
import pytest
import logging
from unittest.mock import patch, mock_open
import sys

# Ensure `src` is correctly found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from src import log_monitor  # Import after fixing path issue

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../config/config.json")

def test_load_config_valid():
    """Test that load_config correctly sets global variables."""
    config_data = {
        "log_file": "logs/server_logs.txt",
        "alert_log_file": "logs/alert_log.txt",
        "alert_threshold": 5,
        "check_interval": 3
    }

    with patch("builtins.open", mock_open(read_data=json.dumps(config_data))):
        log_monitor.load_config(CONFIG_PATH)

    assert log_monitor.LOG_FILE == "logs/server_logs.txt"
    assert log_monitor.ALERT_LOG_FILE == "logs/alert_log.txt"
    assert log_monitor.ALERT_THRESHOLD == 5
    assert log_monitor.CHECK_INTERVAL == 3

def test_setup_logging_valid():
    """Test that setup_logging configures logging properly."""
    with patch("logging.basicConfig") as mock_basic:
        log_monitor.ALERT_LOG_FILE = "logs/alert_log.txt"
        log_monitor.setup_logging()
        mock_basic.assert_called_once_with(
            filename="logs/alert_log.txt",
            level=logging.WARNING,  # Update level to match your code (e.g., WARNING)
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
