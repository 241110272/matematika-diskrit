import math

def dectobin(nums):
    return [bin(num)[2:] for num in nums]

ex1_soal = [321, 1023, 100632]
ex1_hasil = dectobin(ex1_soal)
print("Exercise 1 :")
for i in range(len(ex1_soal)):
    print(f"{i+1}) {ex1_soal[i]} in binary = {ex1_hasil[i]}")