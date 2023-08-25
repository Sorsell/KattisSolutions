stringLength = int(input())
string = input().strip()
dictionary = {"(": ")", "{": "}", "[": "]"}
stack = []
done = True

for i in range(stringLength):
    if string[i] == " ":
        continue
    else:
        if string[i] in dictionary:
            stack.append(string[i])
        else:
            if len(stack) != 0:
                closing = dictionary[stack.pop()]
                if closing == string[i]:
                    continue
                else:
                    print(string[i], i)
                    done = False
                    break
            else:
                print(string[i], i)
                done = False
                break
if done:
    print("ok so far")