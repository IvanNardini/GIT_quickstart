#!/usr/bin/env python

# main libraries
import os
import sys


def check_reboot():
    """Returns True if computer has a pending reboot"""
    return os.path.exists("/run/reboot-require")


def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    print('Everything ok.')
    sys.exit(0)


if __name__ == '__main__':
    main()
