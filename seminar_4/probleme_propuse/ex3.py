#a)
def reducere(L):
    for x in range(len(L)):
        if L[x][2] < 2000:
            L[x][3] = round((8 * L[x][3])/10, 2)

L_carti=[["The Twelve Chairs", ["Ilya Ilf", "Yevgen Petrov"], 1928, 19.99], ["The Alchemist", ["Paulo Coelho"], 1988, 15.00], ["The Kite Runner", ["Khaled Hosseini"], 2003, 27.50], ["1984", ["George Orwell"], 1949, 19.99], ["The Silent Patient", ["Alex Michaelides", "Alicia Berenson"], 2019, 27.99], ["The Road", ["Cormac McCarthy"], 2005, 18.75], ["The Girl with the Dragon Tattoo", ["Stieg Larsson"], 2005, 24.99], ["The Hitchhiker's Guide to the Galaxy", ["Douglas Adams", "Mark Carwardine", "Zaphod Beeblebrox"], 1979, 21.50], ["To Kill a Mockingbird", ["Harper Lee"], 1960, 21.95]]
reducere(L_carti)
for carte in L_carti:
    print(*carte)
#b)
def cheie1(t):
    return (-t[2], t[0])#(desc an aparitie, cresc titlu)
L1 = sorted(L_carti, key=cheie1)
print(L1)
def cheie2(t):
    return (len(t[1]), -t[3])#(cres nr autori, desc preturi)
L2 = sorted(L_carti, key=cheie2)
print(L2)
def cheie3(t):
    L_prim_autor = t[1][0].split()
    return (L_prim_autor[1], L_prim_autor[0], t[0], t[2])
#(cresc nume prim autor, cresc prenume prim autor, cresc titlu, cresc an aparitie)
L3 = sorted(L_carti, key=cheie3)
print(L3)
