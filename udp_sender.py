import socket
import json
import random
import time
from datetime import datetime

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

malicious_ips = ["185.142.53.35", "45.155.205.233", "194.87.237.5", "5.188.87.45"]


def generate_log():
    is_suspicious = random.random() < 0.3
    threat_types = ["Ransomware", "DDoS", "Port Scan", "Brute Force"]

    return {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'dest_ip': random.choice(malicious_ips) if is_suspicious else "8.8.8.8",
        'is_suspicious': is_suspicious,
        'threat_type': random.choice(threat_types) if is_suspicious else "Normal"
    }


print(f"🚀 Sending UDP data to {UDP_IP}:{UDP_PORT}")
print("Press Ctrl+C to stop\n")

try:
    while True:
        data = generate_log()
        sock.sendto(json.dumps(data).encode(), (UDP_IP, UDP_PORT))

        status = "🚨 SUSPICIOUS" if data['is_suspicious'] else "✅ NORMAL"
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {status} - {data['dest_ip']} ({data['threat_type']})")

        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopped.")
    sock.close()