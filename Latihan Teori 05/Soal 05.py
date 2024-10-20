import math

def euler_totient(n):
    result = n
    for p in range(2, int(math.sqrt(n)) + 1):
        if  n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
    if n > 1:
        result -= result // n
    return result

lat5_soal = [29, 49, 77, 169, 1717, 65537]
lat5_hasil = [euler_totient(num) for num in lat5_soal]
print("Soal 5:")
for i in range(len(lat5_soal)):
    print(f"{i+1}) ϕ{lat5_soal[i]} = {lat5_hasil[i]}")