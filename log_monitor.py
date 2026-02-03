# Level 6: Correlation & Time-Window Detection

from datetime import datetime

log_file = "auth.log"
TIME_WINDOW_SECONDS = 120  # 2 minutes

attack_tracker = {}
error_count = 0

with open(log_file, "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        parts = line.split()

        # Parse timestamp safely
        timestamp = datetime.strptime(
            parts[0] + " " + parts[1],
            "%Y-%m-%d %H:%M:%S"
        )

        if "failed" in line:
            ip = line.split("ip=")[1].split()[0]
            port = line.split("port=")[1].strip()
            key = f"{ip}:{port}"

            if key not in attack_tracker:
                attack_tracker[key] = []

            attack_tracker[key].append(timestamp)

        if "error" in line:
            error_count += 1

with open("auto_security_report.txt", "w") as report:
    report.write("SECURITY LOG ANALYSIS REPORT (LEVEL 6)\n")
    report.write("====================================\n\n")

    for key, times in attack_tracker.items():
        times.sort()
        first_seen = times[0]
        last_seen = times[-1]
        duration = (last_seen - first_seen).seconds
        attempts = len(times)

        if attempts >= 5 and duration <= TIME_WINDOW_SECONDS:
            severity = "HIGH"
        elif attempts >= 3 and duration <= TIME_WINDOW_SECONDS:
            severity = "MEDIUM"
        else:
            severity = "LOW"

        report.write(f"Target: {key}\n")
        report.write(f"Severity: {severity}\n")
        report.write(f"Attempts: {attempts}\n")
        report.write(f"Attack Window: {duration} seconds\n")
        report.write(f"First Seen: {first_seen}\n")
        report.write(f"Last Seen: {last_seen}\n")
        report.write("-" * 45 + "\n")

    report.write(f"\nTotal error events detected: {error_count}\n")
