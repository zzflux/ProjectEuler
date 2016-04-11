#Project Euler problem #79
#Passcode derivation
#Status: solved

FILENAME = "e79-keylog.txt"

def checkConsistent(password, loginList):
    for login in loginList:
        index = -1
        temppw = str(password)
        for c in str(login):
            index = temppw.find(c)
            if index == -1:
                return False
            temppw = temppw[index + 1:]
    return True

def passwordGenerator(charSet):
    length = 1
    while True:
        indexList = [0] * length
        first = True
        while not all([x == 0 for x in indexList]) or first:
            first = False
            yield ''.join([charSet[i] for i in indexList])
            for i in range(len(indexList) - 1, -1, -1):
                indexList[i] += 1
                if indexList[i] == len(charSet):
                    indexList[i] = 0
                else:
                    break
        length += 1

def genCharSet(fname):
    charSet = []
    file = open(fname, 'r')
    for line in file:
        for c in line[:-1]:
            if not c in charSet:
                charSet.append(c)
    return charSet
    file.close()

def readLoginList(fname):
    f = open(fname)
    ret = [line[:-1] for line in f]
    f.close()
    return ret

if __name__ == "__main__":
    listOfLogins = readLoginList(FILENAME)
    for cand in passwordGenerator(genCharSet(FILENAME)):
        if checkConsistent(cand, listOfLogins):
            print("Password:", cand, "is consistent.")
            break

                    
#done
