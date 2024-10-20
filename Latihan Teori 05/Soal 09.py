import math

def hextobin(nums):
    return [bin(int(num, 16))[2:] for num in nums]

q9 = ["80E", "ABBA", "135AB", "DEFACED"]
q9Res = hextobin(q9)
print("Soal 9:")
for i in range(len(q9)):
    print(f"{i+1} {q9[i]} dalam binary: {q9Res[i]}")