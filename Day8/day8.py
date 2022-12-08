import sys
from collections import defaultdict
infile = sys.argv[1] if len(sys.argv)>1 else 'day8.in'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]

Gr = []
for line in lines:
    row = line
    Gr.append(row)

DIR = [(-1,0),(0,1),(1,0),(0,-1)]
R = len(Gr)
C = len(Gr[0])

part1 = 0
for r in range(R):
    for c in range(C):
        vis = False
        for (dr,dc) in DIR:
            rr = r
            cc = c
            ok = True
            while True:
                rr += dr
                cc += dc
                if not (0<=rr<R and 0<=cc<C):
                    break
                if Gr[rr][cc] >= Gr[r][c]:
                    ok = False
            if ok:
                vis = True
        if vis:
            part1 += 1
print(part1)

part2 = 0
for r in range(R):
    for c in range(C):
        score = 1
        for (dr,dc) in DIR:
            dist = 1
            rr = r+dr
            cc = c+dc
            while True:
                if not (0<=rr<R and 0<=cc<C):
                    dist -= 1
                    break
                if Gr[rr][cc]>=Gr[r][c]:
                    break
                dist += 1
                rr += dr
                cc += dc
            score *= dist
        part2 = max(part2, score)
print(part2)