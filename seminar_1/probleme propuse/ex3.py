'''Fie 𝑥 și 𝑦 două numere naturale nenule. Calculați numărul biților din reprezentarea
binară a numărului 𝑥 a căror valoare trebuie comutată pentru a obține numărul 𝑦. '''

x = int(input("x="))
y = int(input("y="))
t = x ^ y # va indica bitii diferiti, marcati la nivel de sintaxa cu 1
k = 0
while t != 0:
    # daca bitul de paritate este nenul,
    # inseamna ca e o val de 1 ce indica diferenta de biti a val x si y
    if t & 1 == 1:
        k += 1 # un bit ce trebuie comutat
    t = t >> 1 # deplasare dreapta
print(f"Numarul de biti diferiti din reprezentarile lui x={bin(x)} si y={bin(y)} este k={k}")


