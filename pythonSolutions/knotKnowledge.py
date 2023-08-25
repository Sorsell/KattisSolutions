nOfKnots = int(input())
knots = set(input().split())
knotsLearned = input().split()

for knot in knotsLearned:
    knots.remove(knot)

print(knots.pop())