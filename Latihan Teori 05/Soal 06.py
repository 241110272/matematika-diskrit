import math

def dectobin(nums):
    return [bin(num)[2:] for num in nums]

q6 = [321, 1023, 100632]
q6Res = dectobin(q6)
print("Exercise 1 :")
for i in range(len(q6)):
    print(f"{i+1}) {q6[i]} in binary = {q6Res[i]}")