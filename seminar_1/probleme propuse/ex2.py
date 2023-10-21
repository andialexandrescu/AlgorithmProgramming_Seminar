'''Să se calculeze numărul 𝑥 obținut prin aplicarea operatorului XOR între toate
elementele tuturor submulțimilor mulțimii 𝐴 = {𝑎1, 𝑎2, … , 𝑎𝑛} ⊂ ℕ, mai puțin mulțimea vidă.
De exemplu, dacă 𝐴 = {2, 7, 18} vom obține numărul x = (2) ^ (7) ^ (18) ^ (2 ^ 7) ^ (2
^ 18) ^ (7 ^ 18) ^ (2 ^ 7 ^ 18) = 0 (am folosit parantezele doar pentru a pune în evidență
elementele submulțimilor lui A)'''

input_str = input("Elementele multimii:")
v = input_str.split()
v = [int(num) for num in v]
# print("Lista:", v)

x_xor_y = a_xor_b = 0

# var 1
for x in v:
    a_xor_b = a_xor_b ^ x # 2^7^18
p = 2**(len(v)-1)
while p != 0:
    # print(x_xor_y, "^", a_xor_b, end=" = ")
    x_xor_y = x_xor_y ^ a_xor_b # valcurenta ^ 2^7^18
    p -= 1
print(x_xor_y)

# var 2
'''n = len(v) # lungimea listei
for i in range(0, n):
    p = 2**(n-1)
    while p != 0:
        # print(x_xor_y, "^", v[i], end = " = ")
        x_xor_y = x_xor_y ^ v[i]
        p -= 1
print(x_xor_y)'''
