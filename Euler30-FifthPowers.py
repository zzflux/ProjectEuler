#Project Euler problem #30
#Digit fifth powers
#Status: solved

answer = sum([x for x in range(2, 10**7) if sum([int(d) ** 5 for d in str(x)]) == x])
print("Answer:", answer)

#done
