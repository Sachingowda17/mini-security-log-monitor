# Mini Security Log Monitor (Python)

log_file = "auth.log"

failed_count = 0
error_count = 0

with open(log_file, "r") as file:
    for line in file:
        if "failed" in line:
            failed_count += 1
        if "error" in line:
            error_count += 1

report = open("auto_security_report.txt", "w")

report.write("SECURITY LOG ANALYSIS\n")
report.write("---------------------\n")
report.write(f"Failed login attempts: {failed_count}\n")
report.write(f"Error events: {error_count}\n")

if failed_count >= 3:
    report.write("ALERT: Possible brute-force attack detected\n")

if error_count > 0:
    report.write("NOTE: System errors found\n")

report.close()


