'''Fișierul text exemplu.txt conține un text pe mai multe linii, cuvintele fiind despărțite între ele prin spații și semnele de punctuație uzuale. Implementați un program care să scrie în fișierul text grupe_cuvinte.txt cuvintele distincte (fără duplicate) din fișierul dat, grupate după lungimile lor. Grupele se vor scrie în fișier în ordinea descrescătoare a lungimilor cuvintelor, iar în fiecare grupă cuvintele vor fi scrise în ordine alfabetică.'''

try:
    f = open("exemplu.txt")
    text = f.read().lower() # atunci cand citim din fisier nu facem distinctia intre literele mici si mari
    f.close()
except FileNotFoundError:
    print("Fisier inexistent!")
    exit(0)

sep = ",.:;!?"
d = {}

for ch in sep:
    text = text.replace(ch, " ")

for cuv in text.split():
    cheie = len(cuv)
    if cheie not in d:
        d[cheie] = set([cuv])
    else:
        d[cheie].add(cuv)

'''function cheiedesc_alfabetic is designed to sort strings primarily 
based on their length in descending order (-t[0]) and, 
in case of a tie in length, to break the tie by sorting 
lexicographically in ascending order (t[1])'''

def cheiedesc_alfabetic(t):
    return (-t[0], t[1])

aux = []
aux = sorted(((k, sorted(v)) for (k, v) in d.items()), key=cheiedesc_alfabetic)

f = open("grupe_cuvinte.txt", "w")
for x in aux:
    f.write(f"Lungime {x[0]}: {', '.join(x[1])}\n")
f.close()