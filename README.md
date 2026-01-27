# Mini Security Log Monitor 

This project simulates basic security log monitoring performed by SOC analysts.

## Project Description
The project analyzes authentication logs to:
- Detect failed login attempts
- Identify system errors
- Summarize findings in a security report

## Files in this Project
- auth.log → Sample authentication log data
- security_report.txt → Analysis report based on log findings

## Tools Used
- Linux
- grep
- basic log analysis

## Cybersecurity Relevance
Log monitoring and analysis are core responsibilities in Security Operations Center (SOC) roles.
This project demonstrates how suspicious activity can be detected from system logs.

## Level 2 Automation (Python)

This project includes a Python script that automates log monitoring.

### What the script does
- Reads authentication logs
- Counts failed login attempts
- Counts system errors
- Detects possible brute-force attacks
- Generates an automated security report

### File added
- log_monitor.py → Python-based log monitoring script
- auto_security_report.txt → Automatically generated report

## Level 3: IP-Based Attack Detection

The project was extended to track failed login attempts by IP address.

### Features
- Extracts IP addresses from logs
- Counts failed logins per IP
- Detects potential brute-force attackers
- Generates SOC-style security reports

This simulates real-world SOC detection logic used in security monitoring.

