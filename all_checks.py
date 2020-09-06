#!/usr/bin/env python

# main libraries
import os
import shutil
import sys

def check_reboot():
    """Returns True if computer has a pending reboot"""
    return os.path.exists("/run/reboot-require")

def check_disk_full(disk, min_gb, min_percent):
    """Returns True if there isn't enough disk space, False otherwise"""
    du = shutil.disk_usage(disk)
    # Calculate the % of free space
    percent_free = 100 * du.free / du.total
    # Calculare free gigabytes
    GB_free = du.free / 2**30
    if percent_free < min_percent or GB_free < min_gb:
        return True
    return False

def check_root_full():
    """Returns True if the root partition is full, False otherwise"""
    return check_disk_full(disk="/", min_gb=2, min_percent=10)
    

def main():
    checks = [(check_reboot, 'Pending Reboot.'),
              (check_root_full, 'Root partition full.')]

    everything_ok = True

    for ck, msg in checks:
        if ck():
            print(msg)
            everything_ok = False

    if not everything_ok:
        sys.exit(1)

    print("Everything ok.")
    sys.exit(0)

if __name__ == '__main__':
    main()
