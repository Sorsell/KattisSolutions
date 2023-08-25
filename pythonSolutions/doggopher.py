import sys
# function for calculating distance between two points
def distance(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)


def main():

    coordinatesGopher = []
    coordinatesDog = []
    coordinates = sys.stdin.readline().split()
    for coordinate in enumerate(coordinates):
        #first two coordinates are for gopherä
        if coordinate[0] < 2:
            coordinatesGopher.append(float(coordinate[1]))
        else:
            coordinatesDog.append(float(coordinate[1]))
    coordinatesHoles = []
    while True:
        try:
            value = sys.stdin.readline().split()
            if not value:
                raise ValueError
            coordinatesHoles.append((float(value[0]),float(value[1])))
        except ValueError:
            break
    
    for hole in coordinatesHoles:
        #since we are using squared distance, dog can reach the gopher if 4*distance 
        if 4*distance(coordinatesGopher[0],coordinatesGopher[1],hole[0],hole[1]) <= distance(coordinatesDog[0],coordinatesDog[1],hole[0],hole[1]):
            holeFormatted = format(hole[0],'.3f'),format(hole[1],'.3f')
            print(f"The gopher can escape through the hole at ({holeFormatted[0]},{holeFormatted[1]}).")
            return
        
    print("The gopher cannot escape.")



if __name__ == "__main__":
    main()