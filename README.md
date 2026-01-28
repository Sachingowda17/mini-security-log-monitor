# Mini Security Log Monitor 

A multi-level Python-based security log monitoring project that simulates real-world SOC (Security Operations Center) detection workflows.

This project evolves step by step from basic log analysis to advanced SOC-style alerting with severity and timestamps.

---

## 📌 Project Overview
The Mini Security Log Monitor analyzes authentication logs to detect suspicious activity such as:
- Failed login attempts
- System error events
- Brute-force attacks
- Attacks targeting specific services (SSH, FTP)
- Time-based attack patterns with severity classification

The project demonstrates how SOC analysts monitor logs, track attackers, and generate actionable security reports.

---

## 🧱 Project Evolution (Levels 1 → 5)

### 🔹 Level 1: Manual Log Analysis
**Goal:** Understand how security analysts read logs.

**What was done:**
- Manually analyzed authentication logs
- Identified failed login attempts
- Detected system errors
- Wrote a basic security report

**Skills learned:**
- Log reading
- Pattern identification
- Security reporting fundamentals

---

### 🔹 Level 2: Python Automation
**Goal:** Automate log analysis using Python.

**What was added:**
- Python script to read log files
- Automatic counting of failed logins and errors
- Automated generation of security reports

**Skills learned:**
- Python file handling
- Basic detection logic
- Security automation concepts

---

### 🔹 Level 3: IP-Based Attack Detection
**Goal:** Identify attackers using IP addresses.

**What was added:**
- IP address extraction from logs
- Tracking failed login attempts per IP
- Detection of potential brute-force attackers

**Skills learned:**
- IP-based analysis
- Brute-force detection logic
- SOC-style attacker tracking

---

### 🔹 Level 4: Port-Aware Attack Detection
**Goal:** Detect which services are under attack.

**What was added:**
- Port extraction from logs
- Detection of attacks per IP and port
- Identification of targeted services (SSH – port 22, FTP – port 21)

**Skills learned:**
- Service-level security monitoring
- Port-aware attack analysis
- Advanced SOC detection logic

---

### 🔹 Level 5: Timestamped Alerts & Severity
**Goal:** Add time context and alert severity.

**What was added:**
- Timestamp parsing from logs
- First-seen and last-seen tracking
- Severity classification (LOW / MEDIUM / HIGH)
- SOC-style alert reporting with time context

**Skills learned:**
- Time-based attack analysis
- Alert prioritization
- SOC incident severity assessment

---

## ⚙️ How the System Works
1. Reads authentication logs (`auth.log`)
2. Extracts:
   - Timestamp
   - Username
   - IP address
   - Service port
3. Tracks failed login attempts per IP and port
4. Assigns severity based on attack frequency
5. Generates an automated SOC-style security report

---

## 📂 Project Structure

