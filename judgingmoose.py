left,right = (input().strip().split())
left = int(left)
right = int(right)

if left == 0 and right == 0:
    print("Not a moose")
elif left == right:
    print("Even", right*2)
else:
    print("Odd",max(left,right)*2)