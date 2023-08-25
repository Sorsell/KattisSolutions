import collections
height,width = map(int,input().split())
grid = []
for i in range(height):
    row = input()
    row = list(map(int,row))
    grid.append(row)
steps = []
for i in range(height):
    row = []
    for position in range(width):
        row.append(99999999)
    steps.append(row)
steps[0][0] = 0
specialQueue = collections.deque()
#give start position
specialQueue.append((0,0,0))

while specialQueue:
    currentRow, currentColumn, value = specialQueue.popleft()
    position = grid[currentRow][currentColumn]

    directions = [(0, position), (0, -position), (-position, 0), (position, 0)]

    for changeRow, changeColumn in directions:
        rowNew, columnNew = currentRow + changeRow, currentColumn + changeColumn

        if 0 <= rowNew < height and 0 <= columnNew < width and steps[rowNew][columnNew] > value + 1:
            steps[rowNew][columnNew] = value + 1
            specialQueue.append((rowNew, columnNew, value + 1))

val = steps[height-1][width-1]

if val < 99999999:
    print(val)
else:
    print(-1)