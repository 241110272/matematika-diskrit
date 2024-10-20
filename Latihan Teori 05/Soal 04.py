import math

def lcm(x, y):
    return abs(x*y)

Lat4_soal = [(168,278), (782,8192), (6916,18928)]
Lat4_hasil = [lcm(a, b) for a, b in Lat4_soal]
print("Latihan 4 :")
for i in range(len(Lat4_soal)):
    print(f"{i+1}) LCM{Lat4_soal[i]} = {Lat4_hasil[i]}")