#!/usr/bin/env python3

import csv
from distance import distance

def to_coord(csv):
    return ((float(csv[24]), float(csv[25])))

with open('data.csv') as file:
    reader = csv.reader(file, delimiter=';')
    dist = 0
    old_coord = to_coord(next(reader))
    for row in reader:
        coord = to_coord(row)
        dist += distance(old_coord, coord)
        old_coord = coord
    print(dist)
