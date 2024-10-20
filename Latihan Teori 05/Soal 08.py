import math

def octtobin(nums):
    return [oct(int(num, 8))[2:] for num in nums]

q8 = ["11110111", "101010101010", "111011101110111", "101010101010101"]
q8Res = octtobin(q8)
print("Soal 8:")
for i in range(len(q8)):
    print(f"{i+1}) {q8[i]} dalam binary: {q8Res[i]}")