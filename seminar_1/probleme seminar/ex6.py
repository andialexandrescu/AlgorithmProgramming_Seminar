'''Să se calculeze numărul 𝑥 obținut prin aplicarea operatorului XOR între toate
elementele tuturor submulțimilor mulțimii 𝐴 = {1,2, … , 𝑛} ⊂ ℕ, mai puțin mulțimea vidă.
De exemplu, dacă 𝑛 = 3 obținem 𝑥 = (1)^(2)^(3)^(1^2)^(1^3)^(2^3)^(1^2^3) = 0
(am folosit parantezele doar pentru a pune în evidență elementele submulțimilor lui A).'''

n = int(input("n="))
x_xor_y = 0
for x in range(1, n+1):
    p = 2**(n-1)
    while p != 0:
        x_xor_y = x_xor_y ^ x
        p -= 1
print(x_xor_y)
