nOfMeasurements, expectedVariation = input().split()
nOfMeasurements = int(nOfMeasurements)
expectedVariation = int(expectedVariation)

measurements = list(map(int, input().split()))

maxDiffs = [-float("inf")] * nOfMeasurements

currentDifferencePos = measurements[0] - expectedVariation
currentDifferenceNeg = -measurements[0] - expectedVariation

for i in range(nOfMeasurements):
    adjustedDiffPos = measurements[i] - expectedVariation * (i + 1)
    adjustedDiffNeg = -measurements[i] - expectedVariation * (i + 1)

    currentDifferencePos = min(currentDifferencePos, adjustedDiffPos)
    maxDiffs[i] = max(maxDiffs[i], adjustedDiffPos - currentDifferencePos)

    currentDifferenceNeg = min(currentDifferenceNeg, adjustedDiffNeg)
    maxDiffs[i] = max(maxDiffs[i], adjustedDiffNeg - currentDifferenceNeg)

print(*maxDiffs)
