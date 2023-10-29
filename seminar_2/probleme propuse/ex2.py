'''Se citește o propoziție sau o frază în care cuvintele sunt despărțite
între ele prin spații și semnele de punctuație uzuale. Să se afișeze numărul
cuvintelor distincte din propoziția sau fraza dată. De exemplu, în propoziția
"Ana are prune și gutui verzi, dar mai multe prune decât gutui!" sunt 10 cuvinte
distincte (cuvintele "prune" și "gutui" se iau în considerare o singură data, deși
apar de câte două ori în propoziție).'''

s = input("sir=")
separatori = ",.:;!?"
for c in separatori:
    s = s.replace(c, " ")
rez = " "
k = 0
for cuv in s.split():
    if " " + cuv + " " not in rez:
        rez += cuv + " "
        k += 1
rez = rez.strip()
L = rez.split()
print("Numarul valorilor distincte din propozitie este:", k ,", acestea fiind:", L)

