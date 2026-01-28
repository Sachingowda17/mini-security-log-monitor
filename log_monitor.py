# Level 5: Timestamped Alerts with Severity

log_file = "auth.log"
attack_tracker = {}
error_count = 0

with open(log_file, "r") as file:
    for line in file:
        if not line.strip():
            continue   # skip empty lines safely

        parts = line.strip().split()

        if len(parts) < 2:
            continue   # skip malformed lines

        timestamp = parts[0] + " " + parts[1]

        if "failed" in line:
            ip = line.split("ip=")[1].split()[0]
            port = line.split("port=")[1].strip()
            key = f"{ip}:{port}"

            if key not in attack_tracker:
                attack_tracker[key] = {
                    "count": 0,
                    "first_seen": timestamp,
                    "last_seen": timestamp
                }

            attack_tracker[key]["count"] += 1
            attack_tracker[key]["last_seen"] = timestamp

        if "error" in line:
            error_count += 1

with open("auto_security_report.txt", "w") as report:
    report.write("SECURITY LOG ANALYSIS REPORT (LEVEL 5)\n")
    report.write("====================================\n\n")

    for key, data in attack_tracker.items():
        count = data["count"]
        first_seen = data["first_seen"]
        last_seen = data["last_seen"]

        if count >= 5:
            severity = "HIGH"
        elif count >= 3:
            severity = "MEDIUM"
        else:
            severity = "LOW"

        report.write(f"Target: {key}\n")
        report.write(f"Severity: {severity}\n")
        report.write(f"Attempts: {count}\n")
        report.write(f"First Seen: {first_seen}\n")
        report.write(f"Last Seen: {last_seen}\n")
        report.write("-" * 40 + "\n")

    report.write(f"\nTotal error events detected: {error_count}\n")

