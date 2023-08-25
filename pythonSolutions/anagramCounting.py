import sys
import math

for line in sys.stdin:
    textString = line.strip()
    frequencies = {}
    
    # Calculate character frequencies
    for char in textString:
        frequencies[char] = frequencies.get(char, 0) + 1
    
    # Calculate total anagrams for the current word
    answer = math.factorial(len(textString))
    for charFreq in frequencies.values():
        answer = answer // math.factorial(charFreq)    
    # Print the total number of unique anagrams
    print(answer)