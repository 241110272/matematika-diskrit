import math

def bintodec(nums):
    return [int(num, 2) for num in nums]

q7 = ["11111", "1000000001", "101010101", "110100100010000"]
q7Res = bintodec(q7)
print("Soal 7:")
for i in range(len(q7)):
    print(f"{i+1}) {q7[i]} in decimal = {q7Res[i]}")