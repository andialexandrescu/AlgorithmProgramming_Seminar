'''Fie 𝑛 un număr natural. Să se determine cea mai mică putere a lui 2 mai mare sau egală
decât numărul 𝑛.'''

n = int(input("n="))
k = 0
if n and not (n & (n - 1)):
    p = n
else :
    while n != 0:
        n = n >> 1
        k += 1
    p = 1 << k
print(f"Cea mai mica valoare 2^p>=n este {p}")
