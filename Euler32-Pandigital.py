#Project Euler problem #32
#Pandigital products
#Status: solved

def setIsPandigital(lst, digits):
    used = [False] * len(str(digits))
    for n in lst:
        for d in str(n):
            index = str(digits).find(d)
            if index == -1 or used[index]:
                return False
            used[index] = True
    return all(used)

if __name__ == "__main__":
    print("working...")
    already = []
    for a in range(1, 10 ** 7):
        #print("a =", a)
        for b in range(10 ** (9 - 1 - len(str(a)))):
            if setIsPandigital([a, b, a * b], 123456789) and a * b not in already:
                print(a, "x", b, "=", a * b)
                already.append(a * b)
            if len(str(a * b)) + len(str(a)) + len(str(b)) > 9:
                break
    print("Answer:", sum(already))
#done
