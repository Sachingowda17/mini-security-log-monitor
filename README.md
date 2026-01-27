# Mini Security Log Monitor 

A Python-based security log monitoring project that simulates real-world SOC (Security Operations Center) detection workflows.

---

##  Project Overview
This project analyzes authentication logs to detect suspicious security activity such as:
- Failed login attempts
- System error events
- Brute-force attacks
- Service-specific attacks using ports (SSH, FTP)

It demonstrates how SOC analysts monitor logs, track attackers by IP address, and identify targeted services.

---

## How It Works
1. Reads authentication log data from `auth.log`
2. Extracts key fields:
   - Username
   - IP address
   - Service port
3. Counts failed login attempts per IP and port
4. Detects brute-force behavior based on thresholds
5. Generates an automated SOC-style security report

---

##  Project Structure
mini-security-log-monitor/
│
├── auth.log # Sample authentication log data
├── log_monitor.py # Python-based detection engine
├── auto_security_report.txt # Automated SOC security report
├── security_report.txt # Manual analysis (Level 1 reference)
└── README.md

---

##  Tools & Technologies
- Linux
- Python 3
- Log analysis
- IP-based detection
- Port-aware attack analysis
- Git & GitHub

---

##  Detection Capabilities (Level 4)
- Failed login detection
- IP-based attacker identification
- Port-aware attack detection
- Brute-force attack detection per service
- Automated SOC-style reporting

---

##  Cybersecurity Relevance
Log monitoring and alerting are core responsibilities in SOC and Blue Team roles.
This project simulates how security analysts:
- Identify malicious IPs
- Detect brute-force attacks
- Analyze which services are targeted
- Generate actionable security reports

---

##  Learning Outcomes
Through this project, I gained hands-on experience in:
- Defensive cybersecurity (Blue Team)
- SOC detection logic
- Security log analysis
- Python automation for security
- GitHub-based project documentation

---

##  Future Enhancements
- Severity levels (Low / Medium / High)
- Timestamp and time-based attack correlation
- Alerting system (email / console)
- SIEM-style correlation logic (Splunk-like)

