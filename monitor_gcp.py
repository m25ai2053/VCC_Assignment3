import psutil
import os
import time

# Assignment Requirements
THRESHOLD = 75.0
CHECK_INTERVAL = 3 
CLOUD_VM_NAME = "your-instance-name" # Change this to your GCP VM name
ZONE = "us-central1-a"               # Change this to your VM's zone

def monitor():
    print(f"--- Monitoring Local VM (Threshold: {THRESHOLD}%) ---")
    while True:
        cpu = psutil.cpu_percent(interval=CHECK_INTERVAL)
        print(f"[Metric] Local CPU: {cpu}%")

        if cpu > THRESHOLD:
            print(f"ALERT: CPU hit {cpu}%. Bursting to Google Cloud...")
            # Command to start your existing GCP VM
            os.system(f"gcloud compute instances start {CLOUD_VM_NAME} --zone={ZONE}")
            print(f"SUCCESS: Cloud VM '{CLOUD_VM_NAME}' is now booting up.")
            break 
        
        time.sleep(1)

if __name__ == "__main__":
    monitor()
