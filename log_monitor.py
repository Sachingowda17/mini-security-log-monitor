# Level 4: IP + Port Based Attack Detection

log_file = "auth.log"
failed_count = 0
error_count = 0
attack_tracker = {}

with open(log_file, "r") as file:
    for line in file:
        if "failed" in line:
            failed_count += 1

            ip = line.split("ip=")[1].split()[0]
            port = line.split("port=")[1].strip()

            key = f"{ip}:{port}"
            attack_tracker[key] = attack_tracker.get(key, 0) + 1

        if "error" in line:
            error_count += 1

with open("auto_security_report.txt", "w") as report:
    report.write("SECURITY LOG ANALYSIS REPORT (LEVEL 4)\n")
    report.write("------------------------------------\n")
    report.write(f"Total failed attempts: {failed_count}\n")
    report.write(f"Total error events: {error_count}\n\n")

    report.write("FAILED ATTEMPTS BY IP & PORT:\n")
    for key, count in attack_tracker.items():
        report.write(f"{key} → {count} failures\n")

    report.write("\nPOTENTIAL BRUTE-FORCE ATTACKS:\n")
    for key, count in attack_tracker.items():
        if count >= 3:
            report.write(f"ALERT: {key} suspected brute-force attack\n")

