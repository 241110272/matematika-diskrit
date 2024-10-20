import math

def hextobin(nums):
    return [bin(int(num, 16))[2:] for num in nums]

q9 = ["80E", "ABBA", "135AB", "DEFACED"]
q9 = hextobin(q9)
print("Exercise 4 :")
for i in range(len(q9)):
    print(f"{i+1} {q9[i]} in binary = {q9Res[i]}")