'''Să se determine în mod eficient numărul de biți nuli din reprezentarea binară a unui
număr natural nenul. De exemplu, reprezentarea binară a numărului 600 este
0b1001011000 și conține 6 biți nuli.'''
n = int(input("n="))

def putere_a_lui_2(n):
    k = 0
    if n and not (n & (n - 1)):
        p = n
    else:
        while n != 0:
            n = n >> 1
            k += 1
        p = 1 << k
    return p

# e necesar a crea o masca pentru ca e imposibil a aplica algoritmul de la
# determinarea val nenule dintr-un numar pt val nule, deoarece instructiunea
# t & 1 == 0 nu are sens

mb = putere_a_lui_2(n) - 1 # masca binara de forma 0b11..11
# print(bin(mb))
t = n ^ mb # am obtinut inversul lui n, adica bitii de 0 au devenit 1 si invers

# numaram val nenule:
k = 0
while t != 0:
    if t & 1 == 1:
        k += 1
    t = t >> 1

print(f"Numarul de valori nule din reprezentarea binara a lui n={bin(n)} este k={k}")