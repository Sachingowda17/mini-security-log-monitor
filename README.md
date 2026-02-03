# Mini Security Log Monitor 🔐

A Python-based cybersecurity project that simulates real-world SOC (Security Operations Center) log monitoring and attack detection workflows.

The project evolves step by step from basic manual log analysis to advanced SOC-grade correlation and time-window based attack detection.

---

## 📌 Project Overview

Modern systems generate large volumes of security logs. Manual log analysis is time-consuming and prone to error.  
This project provides an automated approach to analyze authentication logs, detect suspicious activity, and generate actionable security alerts.

The system detects:
- Failed login attempts
- Brute-force attacks
- Attacker identification using IP addresses
- Service-level attacks using ports
- Time-based attack patterns with severity escalation

---

## 🧱 Project Evolution (Levels 1 – 6)

### 🔹 Level 1: Manual Log Analysis
**Objective:** Understand security logs and identify suspicious activity.

**Features:**
- Manual inspection of authentication logs
- Identification of failed login attempts
- Detection of system errors
- Creation of a basic security report

**Skills Gained:**
- Log interpretation
- Security fundamentals
- SOC awareness

---

### 🔹 Level 2: Automation Using Python
**Objective:** Automate repetitive SOC tasks.

**Features:**
- Python script to read log files
- Automatic counting of failed logins and errors
- Auto-generation of security reports

**Skills Gained:**
- Python file handling
- Automation mindset
- SOC efficiency

---

### 🔹 Level 3: IP-Based Attack Detection
**Objective:** Identify attackers using IP addresses.

**Features:**
- Extraction of IP addresses from logs
- Tracking failed attempts per IP
- Detection of potential brute-force attackers

**Skills Gained:**
- IP analysis
- Attacker attribution
- Blue Team detection logic

---

### 🔹 Level 4: Port-Aware Attack Detection
**Objective:** Identify which services are under attack.

**Features:**
- Extraction of service ports from logs
- IP + port correlation
- Detection of service-specific attacks (e.g., SSH, FTP)

**Skills Gained:**
- Network fundamentals
- Service-level security monitoring
- Advanced SOC detection logic

---

### 🔹 Level 5: Timestamped Alerts & Severity Classification
**Objective:** Add time awareness and alert prioritization.

**Features:**
- Timestamp parsing from logs
- First-seen and last-seen tracking
- Severity classification (LOW / MEDIUM / HIGH)
- SOC-style alert reporting

**Skills Gained:**
- Incident prioritization
- Alert severity assessment
- SOC incident response concepts

---

### 🔹 Level 6: Correlation & Attack Window Detection (Final Level)
**Objective:** Reduce noise and detect real attacks using correlation.

**Features:**
- Time-window based detection (burst attacks)
- Correlation of multiple events
- Severity escalation based on frequency and speed
- Noise reduction using SOC-grade logic

**Skills Gained:**
- Correlation logic
- Attack pattern analysis
- SOC L2-level thinking


## ⚙️ System Workflow

Authentication Logs
↓
Log Parsing & Preprocessing
↓
IP & Port Correlation
↓
Time Window Analysis
↓
Severity Classification
↓
SOC-Style Security Report

---

## 🛠 Tools & Technologies

- Linux
- Python 3
- Security log analysis
- IP and port-based detection
- Time-based correlation logic
- Git & GitHub

---

## 🔐 Detection Capabilities

- Failed login detection
- IP-based attacker identification
- Port-aware service attack detection
- Brute-force attack detection
- Timestamped alerts
- Severity escalation
- SOC-grade correlation and noise reduction

---

## 🎯 Cybersecurity Relevance

This project reflects real-world SOC and Blue Team responsibilities, including:
- Monitoring authentication activity
- Detecting brute-force attacks
- Identifying malicious IPs
- Prioritizing incidents using severity
- Generating actionable security reports

---

## 🚀 Learning Outcomes

Through this project, I gained hands-on experience in:
- Defensive cybersecurity (Blue Team)
- SOC detection workflows
- Security log monitoring
- Python-based automation
- Correlation-based threat detection
- Professional documentation and GitHub workflows

---

## 🔮 Future Enhancements

- Machine learning–based attack classification
- Alert escalation rules
- Email or SIEM-style alerting
- Dashboard visualization
- Integration with SIEM tools


