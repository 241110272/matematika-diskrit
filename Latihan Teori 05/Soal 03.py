import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
    
q3 = [(1, 5), (100, 101), (123, 277), (1529, 14039), (1529, 14038), (11111, 111111)]
q3Res = [gcd(a, b) for a,b in q3]
print("Latihan 3 :")
for i in range(len(q3)):
    print(f"{i+1}) GCD{q3[i]} = {q3Res[i]}")