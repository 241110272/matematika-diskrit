import math

def bintodec(nums):
    return [int(num, 2) for num in nums]

ex2_soal = ["11111", "1000000001", "101010101", "110100100010000"]
ex2_hasil = bintodec(ex2_soal)
print("Exercise 2 :")
for i in range(len(ex2_soal)):
    print(f"{i+1}) {ex2_soal[i]} in decimal = {ex2_hasil[i]}")