import math

vertices = int(input().strip())
# number of intersections is the binomial coefficient of the number of vertices and 4
# 4 becuase each intersection is formed by 4 vertices
answer = math.comb(vertices, 4)
print(answer)