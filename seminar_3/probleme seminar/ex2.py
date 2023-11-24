'''Sa se afiseze elementele comune tuturor liniilor unui tablou bidimensional. De exemplu, daca tablou dimensional este:
2 1 5 1 3
1 4 2 2
2 1 1 6 8
atunci trebuie afisate numerele 1 2, nu neapărat în această ordine. '''

n = int(input("n="))
M = []
for i in range(n):
    linie = [int(x) for x in input().split()]
    M.append(linie)
l = set(M[0]) # init cu prima linie transf in multime
for i in range(1, n):
    l.intersection_update(M[i]) #l = l & set(M[i])
print(l)
