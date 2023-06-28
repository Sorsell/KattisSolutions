def minimum_distance(x, y, x1, y1, x2, y2):
    #setting the distance to infinity to start
    distance = float('inf')

    # Check the vertical edges of the rectangle
    for xi in (x1, x2):
        #if the point is between the vertical edges, the distance is the difference between the x values
        if y1 <= y <= y2:
            distance = min(distance, abs(x - xi))
        else:
            #if the point is not between the vertical edges, the distance is the distance between the point and the closest corner
            for yi in (y1, y2):
                distance = min(distance, ((x - xi) ** 2 + (y - yi) ** 2) ** 0.5)
    
    # Check the horizontal edges of the rectangle
    for yi in (y1, y2):
        #if the point is between the horizontal edges, the distance is the difference between the y values
        if x1 <= x <= x2:
            distance = min(distance, abs(y - yi))
        else:
            #if the point is not between the horizontal edges, the distance is the distance between the point and the closest corner
            for xi in (x1, x2):
                distance = min(distance, ((x - xi) ** 2 + (y - yi) ** 2) ** 0.5)

    return float(distance)


x,y,x1,y1,x2,y2 = map(int, input().strip().split())


print(minimum_distance(x,y,x1,y1,x2,y2))



print(minimum_distance(7,3,0,0,5,4))
print(minimum_distance(6,0,0,2,7,6))
print(minimum_distance(3,-4,-3,-1,-1,2))
