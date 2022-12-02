# Getting data
with open('day2.in') as file:
    rounds = [i.replace(" ", "") for i in file.read().strip().split("\n")]

part1_conditions = {
    "AX":4, "AY":8, "AZ":3, 
    "BX":1, "BY":5, "BZ":9, 
    "CX":7, "CY":2, "CZ":6 
}

p1 = 0

for round in rounds:
    p1 += part1_conditions[round]

part2_conditions = {
    "AX":3, "AY":4, "AZ":8, 
    "BX":1, "BY":5, "BZ":9, 
    "CX":2, "CY":6, "CZ":7 
}

p2 = 0
for round in rounds:
    p2 += part2_conditions[round]