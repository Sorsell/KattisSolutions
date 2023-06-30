import bisect
import sys

#finds the closest sum to a given number
def solve(case, nums, queries):
    possibleSums = []
    for i, a in enumerate(nums):
        for b in nums[i+1:]:
            valueSum = a + b
            possibleSums.append(valueSum)
    possibleSums.sort()
    print(f'Case {case+1}:')
    for q in queries:
        pos = bisect.bisect_left(possibleSums, q)
        diffSum = []
        for i in [pos, pos-1]:
            if 0 <= i < len(possibleSums):
                diff = abs(possibleSums[i] - q)
                diffSum.append((diff, possibleSums[i]))
        closest = min(diffSum)[1]
        print(f'Closest sum to {q} is {closest}.')

def main():
    case = 0
    while True:
        try:
            n = int(sys.stdin.readline())
        except ValueError:
            break
        nums = []
        for i in range(n):
            nums.append(int(input().strip()))
        m = int(input().strip())
        queries = []
        for i in range(m):
            queries.append(int(input().strip()))
        solve(case, nums, queries)
        case += 1

if __name__ == "__main__":
    main()
