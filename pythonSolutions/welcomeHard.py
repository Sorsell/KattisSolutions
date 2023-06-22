def solve(string):
    targetString = 'welcome to code jam'
    array = [0] * (len(targetString) + 1)
    array[0] = 1
    #iterate through the string
    #for each character, iterate through the targetString backwards
    for character in string:
        for i in range(len(targetString) - 1, -1, -1):
            if character == targetString[i]:
                array[i + 1] += array[i]
    # return the last element of the array array
    #%10000 to get the last 4 digits
    return rightFormat(array[-1] % 10000)


# function for formatting the output, adding necessary amount of zeros
def rightFormat(num):
    return "{:04d}".format(num)


nOfTimes = int(input().strip())
for i in range(nOfTimes):
    string = input().strip()
    print('Case #' + str(i + 1) + ': ' + solve(string))
