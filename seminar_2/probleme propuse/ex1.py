'''Se citește un cuvânt w și un șir format din n cuvinte.
Să se afișeze toate cuvintele distincte care au aceeași lungime cu w.
De exemplu, pentru w = "mere" și cuvintele "pere", "teste" și "mure"
(deci n = 3), trebuie să fie afișate cuvintele "pere" și "mure". '''
w = input("cuv=")
n = int(input("n="))
rez = " "

for cuv in range(n):
    cuv = input()
    if len(cuv) == len(w) and (" " + cuv + " " not in rez):
        rez += cuv + " "
rez = rez.strip()
L = rez.split()
print("Cuvintele de aceeasi lungime cu '" + w + "' sunt urmatoarele: '", " ',' ".join(L), "'")