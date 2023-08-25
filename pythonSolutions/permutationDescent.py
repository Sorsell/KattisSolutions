MOD = 1001113

mem = {}

def permutations(intOrder, intValue):
    #create unique index for each permutation, 123 is chosen becuae it is greater then the max value of intOrder
    index = intOrder * 123 + intValue
    if intValue == 0 or intValue == intOrder - 1:
        mem[index] = 1
    #if the value is not in the dictionary
    if index not in mem:
        value1 = (intValue + 1) * permutations(intOrder - 1, intValue)
        value2 = (intOrder - intValue) * permutations(intOrder - 1, intValue - 1)
        mem[index] = (value1 + value2) % MOD
    return mem[index]

nOfDataSets = int(input().strip())
for i in range(nOfDataSets):
    dataSetNumber, intOrder, intValue = map(int, input().strip().split())
    answer = permutations(intOrder, intValue)
    print(f"{dataSetNumber} {answer}")
