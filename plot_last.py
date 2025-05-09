#!/usr/bin/env python3
import sys
from pyrano.application import graphs

def main():
    station = sys.argv[-1]
    path = f"plots/last_radiation_{station}.jpg"
    graphs.plot_today(station, path)

if __name__ == "__main__":
    main()
