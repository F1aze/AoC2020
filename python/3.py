import math

grid = [l.strip() for l in open('../in/3.in')]
res = [sum(grid[v][right*idx % len(grid[0])] == '#' for idx,v in enumerate(range(0, len(grid), down)))
   for right, down in ([1,1], [3,1], [5,1], [7,1], [1,2])]
print(f"Part 1: {res[1]}\nPart 2: {math.prod(res)}")