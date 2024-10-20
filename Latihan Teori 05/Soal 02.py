import math

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n  % i == 0:
            return False
    return True

#Masukkan angka yang ingin dicari bilangan prima-nya kedalam q2

q2 = [21, 71, 111, 29, 97, 143]
q2Res = [prime(num) for num in q2]

print("Soal 2:")
for i in range(len(q2)):
    print(f"{i+1}) {q2[i]} adalah bilangan prima: {q2Res[i]}")
    continue