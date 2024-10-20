import math

def lcm(x, y):
    return abs(x*y)

q4 = [(168,278), (782,8192), (6916,18928)]
q4Res = [lcm(a, b) for a, b in q4]
print("Soal 4:")
for i in range(len(q4)):
    print(f"{i+1}) LCM{q4[i]} = {q4Res[i]}")