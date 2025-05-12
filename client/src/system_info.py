import os
import platform
import time

import psutil


def get_cpu_usage():
    """Return current CPU usage percentage."""
    return f"CPU Usage: {psutil.cpu_percent(interval=1)}%"


def get_memory_info():
    """Return memory usage details in GB."""
    mem = psutil.virtual_memory()
    return (
        f"Memory - Total: {mem.total // (1024**3)} GB, "
        f"Used: {mem.used // (1024**3)} GB, Free: {mem.available // (1024**3)} GB"
    )


def get_system_uptime():
    """Return system uptime in hours and minutes."""
    uptime_seconds = time.time() - psutil.boot_time()
    hours = int(uptime_seconds // 3600)
    minutes = int((uptime_seconds % 3600) // 60)
    return f"Uptime: {hours} hours, {minutes} minutes"


def get_disk_usage():
    """Return disk usage details for the root drive in GB."""
    disk = psutil.disk_usage("C:\\" if os.name == "nt" else "/")
    return (
        f"Disk Usage - Total: {disk.total // (1024**3)} GB, "
        f"Used: {disk.used // (1024**3)} GB, Free: {disk.free // (1024**3)} GB"
    )


def check_system_load():
    """Check system load and provide feedback."""
    cpu_load = psutil.cpu_percent(interval=1)
    mem_load = psutil.virtual_memory().percent
    if cpu_load > 80 or mem_load > 85:
        return (
            f"🚨 High load! CPU: {cpu_load}%, Memory: {mem_load}% - "
            "Consider closing some applications."
        )
    return f"System load normal. CPU: {cpu_load}%, Memory: {mem_load}%"


def display_system_info():
    """Display all system information."""
    print("\nSystem Information:")
    print(get_cpu_usage())
    print(get_memory_info())
    print(get_system_uptime())
    print(get_disk_usage())
    print(check_system_load())
    print()


if __name__ == "__main__":
    display_system_info()
