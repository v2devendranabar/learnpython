log_file = [
   "INFO: Operation successful",
   "ERROR: File not found",
   "DEBUG: Connection established",
   "ERROR: Database connection failed",
   "ERROR: Read Latency High",
   "WARN: ENABLE MULTI-AZ Deployment",
   "WARN: ENABLE ENCRYPTION",
   "DEBUG: Storage Class Optimized",
   "ERROR: Resources exhausted"
]

for line in log_file:
  if "ERROr" in line:
    print(line)
  else:
    print("Invalid search pattern")
    break