import sys
from copy import deepcopy
file = sys.argv[1] if len(sys.argv)>1 else 'day6.in'
data = open(file).read()
lines = [x for x in data.split('\n')]

part1 = False
part2 = False
for i in range(len(data)):
    if (not part1) and i-3>=0 and len(set([data[i-j] for j in range(4)]))==4:
        print(i+1)
        part1 = True
    if (not part2) and i-13>=0 and len(set([data[i-j] for j in range(14)]))==14:
        print(i+1)
        part2 = True