#Project Euler problem #42
#Coded triangle numbers
#Solved
#Jon McMahon, April 2016

import string
import math

Letters = string.ascii_uppercase
Filename = 'p042_words.txt'
LongestWordLength = 200 #If they're using words over this many letters long, this script may fail
MaxN = int((-1 + math.sqrt(1 + 8 * (LongestWordLength * len(Letters)))) / 2 + 1)
Triangulars = set((n * (n + 1)) // 2 for n in range(1, MaxN + 1))

if __name__ == '__main__':
    with open(Filename, 'r') as thefile:
        rawdata = thefile.read()
    rawdata = rawdata.strip('"')
    print('Answer:', sum(sum(Letters.index(c) + 1 for c in word) in Triangulars for word in rawdata.split('","')))

