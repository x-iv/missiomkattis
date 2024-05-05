n = int(input()) #no of cells
m = int(input()) #no of lanes
cells = [input() for _ in range(m)]

empty_cell = 0
for row in cells:
    empty_cell += row.count('.')
proportion = empty_cell / (n * m)

print(proportion)
