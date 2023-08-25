import heapq
nOfTimesINeedToAsk , coworkers = map(int, input().split())
currentValues = []
increases = []
heap = []

for i in range(coworkers):
    a,b = map(int, input().split())
    currentValues.append(a)
    increases.append(b)
    heapq.heappush(heap,(a+b,i))

for i in range(nOfTimesINeedToAsk):
    value, minIndex = heapq.heappop(heap)
    currentValues[minIndex] = currentValues[minIndex] + increases[minIndex]
    heapq.heappush(heap,(value+increases[minIndex],minIndex))

print(max(currentValues))