import math

def dectobin(nums):
    return [bin(num)[2:] for num in nums]

q5 = [321, 1023, 100632]
q5Res = dectobin(q5)
print("Exercise 1 :")
for i in range(len(q5)):
    print(f"{i+1}) {q5[i]} in binary = {q5Res[i]}")