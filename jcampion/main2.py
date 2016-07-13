#!/usr/bin/env python3

import csv
from distance import distance
from functools import reduce

def to_coord(csv):
    return ((float(csv[24]), float(csv[25])))

with open('data.csv') as file:
    reader = csv.reader(file, delimiter=';')
    dist = reduce(lambda a, b: (a[0] + distance(to_coord(a[1]), \
        to_coord(b)), b), reader, (0, next(reader)))[0]
    print(dist)
