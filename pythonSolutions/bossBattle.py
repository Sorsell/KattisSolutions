nOfPilars = int(input().strip())
# 3 pillars can be destroyed in 1 shot
if nOfPilars <= 3:
    print(1)
# if greater then 3, then n-2 shots are required
else:
    print(nOfPilars - 2)