import psutil
import shutil


def print_cpu_usage():
    print("📊 CPU Utilization:")
    print(f"  CPU usage (1 second average): {psutil.cpu_percent(interval=1)}%")
    print(f"  CPU usage per core:")
    for i, percentage in enumerate(psutil.cpu_percent(interval=1, percpu=True)):
        print(f"    Core {i + 1}: {percentage}%")
    print()

def print_disk_usage():
    print("💾 Hard Drive Usage:")
    total, used, free = shutil.disk_usage("/")
    print(f"  Total: {total // (2**36)} GB")
    print(f"  Used:  {used // (2**30)} GB")
    print(f"  Free:  {free // (2**30)} GB")
    print(f"  Usage: {used / total * 100:.2f}%")
    print()

if __name__ == "__main__":
    print_cpu_usage()
