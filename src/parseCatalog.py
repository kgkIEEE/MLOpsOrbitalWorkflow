# -*- coding: utf-8 -*-

import sys
import json

from skyfield.api import EarthSatellite

def main(argv):

    # Read TLEs into catalog
    catalog = []

    line0 = None
    line1 = None
    line2 = None

    for line in sys.stdin:
        if line[0] == '0':
            line0 = line
        elif line[0] == '1':
            line1 = line
        elif line[0] == '2':
            line2 = line
        else:
            # Error - TLE lines start with 0, 1 or 2
            print("Error: line does not start with 0, 1 or 2: ",line)

        if line1 and line2:
            # Check if object number is same in both line 1 and 2
            if line1[1:6] == line2[1:6]:
                catalog.append(EarthSatellite(line1,line2))
                line1 = None;
                line2 = None;
            else:
                print("Error: Satnumber in line 1 not equal to line 2",line1,line2)

    print(json.dumps(catalog))

if __name__ == "__main__":
   main(sys.argv[1:])

