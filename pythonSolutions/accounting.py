n,q = map(int,input().strip().split())

#array is a dictionary that stores the value
array = {}
defaultValue = 0

for i in range(q):
    type = input().strip()
    #if string is SET
    if type[0] == "S":
        type,a,b = type.split()
        a,b = int(a),int(b)
        array[a] = b
    #if string is PRINT     
    elif type[0] == "P":
        type,a = type.split()
        a = int(a)
        print(array.get(a,defaultValue))
    #if string is RESTART
    else:
        type,a = type.split()
        defaultValue = int(a)
        array = {}
