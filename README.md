# Hybrid Cloud Auto-Scaling (Cloud Bursting)

##  Overview: Hybrid Cloud Auto-Scaling & Resource Monitoring

##  Objective
* Monitor CPU usage on local VM
* Trigger cloud instance if usage > 75%
* Handle workload using GCP VM

##  Tech Stack
* Python (psutil)
* Google Cloud (Compute Engine)
* gcloud CLI
* Ubuntu (VirtualBox)

##  Working
1. Python script checks CPU usage every 2 seconds
2. If CPU > 75%, it triggers scaling
3. `gcloud` command starts GCP instance
4. Cloud VM handles high workload

##  Author
Vivek Kumar (M.Tech AI)
