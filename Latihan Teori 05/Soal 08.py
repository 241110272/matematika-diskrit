import math

def octtobin(nums):
    return [oct(int(num, 8))[2:] for num in nums]

ex3_soal = ["11110111", "101010101010", "111011101110111", "101010101010101"]
ex3_hasil = octtobin(ex3_soal)
print("Exercise 3 :")
for i in range(len(ex3_soal)):
    print(f"{i+1}) {ex3_soal[i]}  in binary = {ex3_hasil[i]}")