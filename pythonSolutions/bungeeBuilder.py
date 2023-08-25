nOfMountains = int(input())
moutainHeights = list(map(int, input().split()))

maxHeightDiff = 0
possiblePositions = []

start = 0
#iterating from left to right to find possible positions
for i in range(1, nOfMountains):
    if moutainHeights[i] >= moutainHeights[start]:
        possiblePositions.append([start, i])
        start = i

start = nOfMountains - 1
#iterating from right to left to find possible positions
for i in range(nOfMountains - 2, -1, -1):
    if moutainHeights[i] >= moutainHeights[start]:
        possiblePositions.append([i, start])
        start = i

#going through all possible positions and finding the max height difference
for start, end in possiblePositions:
    for i in range(start + 1, end):
            maxHeightDiff = max(maxHeightDiff, min(moutainHeights[start], moutainHeights[end]) - moutainHeights[i])
print(maxHeightDiff)