import itertools
import heapq

#Support Functions
##################
def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def daysOfThatMonth(month, year):
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month == 2:
        if isLeapYear(year):
            return 29
    return days[month-1]

def is_valid(d,m,y):
    if y < 2000:
        return False
    if m < 1 or m > 12:
        return False
    if d < 1 or d > daysOfThatMonth(m, y):
        return False
    return True
##################################
#Main function
counter = int(input())
for i in range(counter,0,-1):
    datesHeap = []
    validDates = set()
    numberString = input().replace(" ", "")
    for permutation in itertools.permutations(numberString):
        day = int("".join(permutation[:2]))
        month = int("".join(permutation[2:4]))
        year = int("".join(permutation[4:]))
        if not is_valid(day,month,year) or (day,month,year) in validDates:
            continue
        validDates.add((day,month,year))
        heapq.heappush(datesHeap, (year,month,day))
    validDates = len(datesHeap)
    if validDates == 0:
        print("0")
    else:
        #heappop gets the earliest date
        year,month,date = heapq.heappop(datesHeap)
        if month < 10:
            month = f"0{month}"
        if date < 10:
            date = f"0{date}"
        print(f"{validDates} {date} {month} {year}")