from datetime import datetime

filtered_log = []
with open("hblog.txt", "r") as f:
    for line in f:
        if "TSTFEED0300|7E3E|0400" in line:
            filtered_log.append(line)

timestamps = []
for line in filtered_log:
    idx = line.find("Timestamp ")
    if idx != -1:
        ts_str = line[idx + 10 : idx + 18]
        ts = datetime.strptime(ts_str, "%H:%M:%S")
        timestamps.append(ts)
timestamps.sort()

with open("hb_test.log", "w") as log_file:
    for i in range(len(timestamps) - 1):
        current = timestamps[i]
        next_time = timestamps[i + 1]
        delta = (next_time - current).total_seconds()

        if delta < 0:
            delta += 24*3600

        if 31 < delta < 33:
            log_file.write(f"WARNING at {current.strftime('%H:%M:%S')}, heartbeat={delta:.0f} sec\n")
        elif delta >= 33 and delta < 100:
            log_file.write(f"ERROR at {current.strftime('%H:%M:%S')}, heartbeat={delta:.0f} sec\n")
