# Level 3: IP-based Security Log Monitor

log_file = "auth.log"

failed_count = 0
error_count = 0
ip_tracker = {}

with open(log_file, "r") as file:
    for line in file:
        if "failed" in line:
            failed_count += 1

            # Extract IP address
            if "ip=" in line:
                ip = line.split("ip=")[1].strip()
                ip_tracker[ip] = ip_tracker.get(ip, 0) + 1

        if "error" in line:
            error_count += 1

# Generate report
with open("auto_security_report.txt", "w") as report:
    report.write("SECURITY LOG ANALYSIS REPORT (LEVEL 3)\n")
    report.write("------------------------------------\n")
    report.write(f"Total failed login attempts: {failed_count}\n")
    report.write(f"Total error events: {error_count}\n\n")

    report.write("FAILED LOGIN ATTEMPTS BY IP:\n")
    for ip, count in ip_tracker.items():
        report.write(f"{ip} → {count} failed attempts\n")

    report.write("\nPOTENTIAL ATTACKERS:\n")
    for ip, count in ip_tracker.items():
        if count >= 3:
            report.write(f"ALERT: {ip} suspected brute-force attacker\n")



