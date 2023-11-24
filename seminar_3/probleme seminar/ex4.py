'''Scrieți un program care construieşte o matrice pătratică M de dimensiune n, având forma următoare:
- pe ultima linie şi ultima coloană toate elementele sunt egale cu 1;
- restul elementelor se calculează ca sumă a elementelor vecine de la est şi sud.

Exemplu: pentru n = 4 matricea ceruta este:
20 10 4 1
10 6 3 1
4 3 2 1
1 1 1 1'''

n = int(input("n="))
M = [[1] * n for x in range(n)]
for i in range(n-2, -1, -1):
    for j in range(n-2, -1, -1):
        M[i][j] = M[i][j+1] + M[i+1][j]
for linie in M:
    print(*linie)
