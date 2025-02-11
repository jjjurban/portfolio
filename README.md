<<<<<<< HEAD
# Portfolio Project
=======
Here's your updated `README.md` with the new config part added:

```markdown
# Log Monitor Alert

This project is a simple log monitoring tool designed to detect suspicious activity based on failed login attempts in a log file. The tool continuously checks the log file for failed login attempts, and if a certain threshold is exceeded, it triggers an alert by writing to a separate log file.

## Features

- Monitors server log files for failed login attempts.
- Alerts when there are multiple failed login attempts from the same IP address.
- Customizable threshold for failed login attempts.
- Generates alerts with timestamps when suspicious activity is detected.

## Prerequisites

- Python 3.x installed on your system.
- Required Python libraries: `re`, `time`, `logging`, and `os`.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/jjjurban/portfolio.git
   ```

2. Navigate to the project directory:
   ```bash
   cd log-monitor-alert
   ```

3. Install dependencies (you can optionally create a virtual environment):
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure that you have a log file (`server_logs.txt`) in the `logs/` directory. The log file should contain logs of login attempts, with failed login attempts matching the pattern:
   ```bash
   Failed login from <IP_ADDRESS>
   ```

## Configuration

A configuration file `config.json` is used to store the script settings. You can adjust these settings based on your environment.

1. The configuration file should be located at: `log-monitor-alert/config/config.json`.
2. You can modify the following settings in the `config.json` file:

   ```json
   {
       "LOG_FILE": "logs/server_logs.txt",
       "ALERT_LOG_FILE": "logs/alert_log.txt",
       "ALERT_THRESHOLD": 3,
       "CHECK_INTERVAL": 2
   }
   ```

   - **LOG_FILE**: Path to the server log file.
   - **ALERT_LOG_FILE**: Path where the alert log will be saved.
   - **ALERT_THRESHOLD**: Number of failed login attempts before triggering an alert (default: 3).
   - **CHECK_INTERVAL**: Time interval (in seconds) between each check of the log file (default: 2).

## How to Use

1. Navigate to the project folder:
   ```bash
   cd /path/to/log-monitor-alert
   ```

2. Run the Python script:
   ```bash
   python src/log_monitor.py
   ```

3. The script will start monitoring the log file (`server_logs.txt`) and will alert you if there are multiple failed login attempts from the same IP address.

## Example Log File

An example of the expected log format is:
```
Failed login from 192.168.1.1
Failed login from 192.168.1.2
Failed login from 192.168.1.1
Failed login from 192.168.1.1
```

## License

MIT License

## Contributing

We welcome contributions! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes.
4. Test your changes.
5. Create a pull request with a description of your changes.

Please make sure your code follows the existing style and includes appropriate tests.

## Acknowledgments

- Python for making it easy to develop this tool.
- Everyone contributing to open-source projects that help make this tool possible.
```

This `README.md` includes the **configuration** section, explaining where to find the config file and what settings can be customized. Feel free to update it with any other details specific to your use case!
>>>>>>> b2c7823 (Initial commit of log-monitor-alert project)
