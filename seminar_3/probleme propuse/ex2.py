'''Scrieți un program care verifică dacă două șiruri de caractere s și t formate doar din litere mici sunt anagrame și, în caz afirmativ, afișează o permutare p prin care șirul t se obține din șirul s, respectiv o permutare q prin care șirul s se obține din șirul t. De exemplu, pentru șirurile s = "emerit" și t = "treime" o permutare p prin care se poate obține șirul t din șirul s este 𝑝=(123456356241), deoarece prima literă din șirul s (litera 'e') trebuie să fie a treia literă din șirul t, a doua literă din șirul s (litera 'm') trebuie să fie a cincea literă din șirul t, ș.a.m.d.'''

import copy
def dictionar_poz(sir, d):
    for lit in list(set(sir)):
        #list_indexes = []
        #for i in range(len(sir)):
            #if lit == sir[i]:
                #list_indexes.append(i+1)
        list_indexes = [i+1 for i in range(len(sir)) if lit == sir[i]]
        d[lit] = list_indexes
    print("Indicii pt fiecare litera din sirul " + sir + " sunt: " + str(d))

s = input("s=")
t = input("t=")
ds = dt = {}
P = [] # permutare
P2 = []

dictionar_poz(s, ds)
print(list(ds.values()))
dt = copy.deepcopy(ds) # dt e complet independent de ds, altfel ds isi pierde valoarea, luand-o pe cea a lui dt
dictionar_poz(t, dt)
print(list(dt.values()), '\n')

P = [[ds[lit] for lit in s],[dt[lit] for lit in s]]
for sublist in P:
    print(*sublist)

#P2 = [[ds[lit][0] for lit in s] for y in range(2)]

#for i in range(len(s)):# ordinea in care apar lit ce reprez cheile in s
    #for list_poz in ds.values():# echivalent for item in ds.values():
#    P2.append(i+1)
#for lit in s:
#    if poz not in *dt:
#        P2.append([dt[lit][poz:] for lit in s])
#print(P2)



