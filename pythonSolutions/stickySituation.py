#function that checks triangle inequality
def valid(side1, side2, side3):
    if side1 < side2 + side3:
        if side2 < side1 + side3:
            if side3 < side1 + side2:
                return True
    return False


nOfSides = input().strip()
sides = list(input().strip().split())

#converts the sides to integers and sorts them from smallest to largest
for i in range(len(sides)):
    sides[i] = int(sides[i])
sides = sorted(sides)

#checks if the triangle is possible
for i in range(len(sides) - 2):
    if valid(sides[i], sides[i + 1], sides[i + 2]):
        print ('possible')
        break
else:
    print('impossible')