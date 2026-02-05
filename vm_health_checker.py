import random

VMs = ["vm-frontend", "vm-backend", "vm-database"]

print("☁️ Cloud VM Health Report\n")

for vm in VMs:
    cpu = random.randint(10, 95)
    memory = random.randint(20, 90)

    status = "HEALTHY"
    if cpu > 80 or memory > 85:
        status = "UNHEALTHY"

    print(f"VM: {vm}")
    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Status: {status}\n")
