import math

def hextobin(nums):
    return [bin(int(num, 16))[2:] for num in nums]

ex4_soal = ["80E", "ABBA", "135AB", "DEFACED"]
ex4_hasil = hextobin(ex4_soal)
print("Exercise 4 :")
for i in range(len(ex4_soal)):
    print(f"{i+1} {ex4_soal[i]} in binary = {ex4_hasil[i]}")