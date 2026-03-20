#!/usr/bin/python3

# This program read a Kicad PCL (POS) output from stdin or from a file
# supplied on the command line and generates a PCL suitable for JLCPCB
# on standard output.  This just involves rearranging the columns and
# changing the column names.
#
# The PCL file must be in CSV format.

import sys
import csv

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin

cf = csv.reader(f)
line = cf.__next__()
if len(line) != 7:
    sys.stderr.write("First line doesn't have 7 values, doesn't appear to be"
                     + " a Kicad POS output")
    sys.exit(1)
    pass

ocf = csv.writer(sys.stdout)

expected_first_line = 'Ref,Val,Package,PosX,PosY,Rot,Side'.split(",")
for i in range(0, len(expected_first_line)):
    if line[i] != expected_first_line[i]:
        sys.stderr.write("First line pos %d: Expected %s, got %s" %
                         (i, expected_first_line[i], line[i]))
        sys.exit(1)
        pass
    pass
ocf.writerow(('Designator', 'Mid X', 'Mid Y', 'Layer', 'Rotation'))

lineno = 1
for line in cf:
    lineno += 1
    if len(line) != 7:
        sys.stderr.write("Line %s doesn't have 7 values, it has %d" %
                         (lineno, len(line)))
        sys.exit(1)
        pass
    rotation = int(float(line[5]))
    ocf.writerow((line[0], line[3], line[4], line[6], rotation))
    pass
