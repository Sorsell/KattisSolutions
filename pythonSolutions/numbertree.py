

#take two or one inputs
path = None
number = input().strip()
if ' ' in number:
    number, path = number.split()
    path = list(path)
number = int(number)

#number of nodes in tree
numOfNodes = 2**(number+1) - 1


index = 0  

#for letters in path
if path:
    for letter in path:
        if letter == 'L':
            index = (2*index)+1
        else:
            index = (2*index)+2

#calculate node value
nodeValue = numOfNodes - index
print(nodeValue)

