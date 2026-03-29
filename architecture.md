+-----------------------------+
|       Local Environment     |
|  (VirtualBox - Ubuntu VM)   |
+-------------+---------------+
              |
              | 1. Resource Monitoring
              v
+-----------------------------+
|   Monitoring Engine         |
|   (Python + psutil script)  |
+-------------+---------------+
              |
              | 2. CPU Usage Check
              v
+-----------------------------+
|   Decision / Trigger Logic  |
|   (Threshold > 75%)         |
+-------------+---------------+
      Yes / Trigger |
                    v
+-----------------------------+
|   Orchestration Layer       |
|   (gcloud CLI / API Call)   |
+-------------+---------------+
              |
              | 3. Start Cloud Instance
              v
+-----------------------------+
|     Cloud Environment       |
|   (GCP Compute Engine VM)   |
|   instance-vivek-gcp        |
+-------------+---------------+
              |
              | 4. Workload Handling
              v
+-----------------------------+
|   Application Deployment    |
| (High CPU Workload Shifted) |
+-----------------------------+
