import math

def mod17(nums):
    return [num % 17 == 0 for num in nums]

q1 = [68, 84,357, 1001]
q1Res = mod17(q1)
print("Soal Pertama:")
for i in range(len(q1)):
    print(f"{i+1}) {q1[i]} % 17 : {q1Res[i]}")
    continue