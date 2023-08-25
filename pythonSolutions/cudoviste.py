nOfRows, nOfColumns = map(int, input().split())
cityMap = []
for i in range(nOfRows):
    cityMap.append(input())

squashCouter = [0, 0, 0, 0, 0]

for row in range(nOfRows - 1):
    for column in range(nOfColumns - 1):
        string = cityMap[row][column:column + 2] + cityMap[row + 1][column:column + 2]
        counter = string.count("X")
        if "#" not in string:
            squashCouter[counter] += 1
print(f"{squashCouter[0]}""\n"f"{squashCouter[1]}""\n"f"{squashCouter[2]}""\n"f"{squashCouter[3]}""\n"f"{squashCouter[4]}")
