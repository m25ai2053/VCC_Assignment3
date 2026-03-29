import psutil
import os
import time

# --- CONFIGURATION ---
THRESHOLD = 75.0        # Assignment Requirement
CHECK_INTERVAL = 2      # Seconds between checks
GCP_VM_NAME = "instance-vivek-gcp"  # Replace with your GCP VM name
GCP_ZONE = "us-central1-c"           # e.g., us-central1-a

def get_cpu_usage():
    # Returns the CPU usage over the last interval
    return psutil.cpu_percent(interval=CHECK_INTERVAL)

def burst_to_cloud():
    print(f"\n[ALERT] CPU usage has exceeded {THRESHOLD}%!")
    print(f"[ACTION] Triggering auto-scale: Starting GCP Instance {GCP_VM_NAME}...")
    
    # Command to start your existing GCP VM
    exit_code = os.system(f"gcloud compute instances start {GCP_VM_NAME} --zone={GCP_ZONE}")
    
    if exit_code == 0:
        print("[SUCCESS] Cloud instance is now running. Load balanced.")
    else:
        print("[ERROR] Failed to start cloud instance. Check gcloud configurations.")

if __name__ == "__main__":
    print(f"Monitoring started. Target Threshold: {THRESHOLD}%")
    try:
        while True:
            usage = get_cpu_usage()
            print(f"Current Local CPU Usage: {usage}%", end="\r")
            
            if usage > THRESHOLD:
                burst_to_cloud()
                break # Stop script after triggering
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
