#Project Euler problem #29
#Distinct powers
#Status: solved

MIN = 2
MAX = 100

if __name__ == "__main__":
    print("Answer:", len(set(a**b for a in range(MIN, MAX + 1) for b in range(MIN, MAX + 1))))
    
    
#done
