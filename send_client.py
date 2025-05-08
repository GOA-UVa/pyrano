#!/usr/bin/env python3
import sys

from client.post_measurements import read_post

def main():
    last_hours = float(sys.argv[-1])
    read_post(last_hours, config_path = 'config.yml')

if __name__ == "__main__":
    main()
