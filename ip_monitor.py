import psutil
import time

blacklisted_ips = {"..."} # <-- insert IP here

logfile = "ip_monitor_log.txt"

def monitor():
    print("Watching for blacklisted IPs... Press CTRL+C to stop")

    while True:
        connections = psutil.net_connections(kind='inet')
        for x in connections:
            if x.status == 'ESTABLISHED' and x.raddr:
                ip = x.raddr.ip
                if ip in blacklisted_ips:
                    print("[!] Detected connection to blacklisted ip:", ip)
                    with open(logfile, "a") as f:
                        f.write(ip + "\n")

        time.sleep(3)

monitor()

