'''Să se afișeze numărul de litere mici, litere mari și semne de punctuație
dintr-o propoziție citită de la tastatură.'''

s = input("sir=")
punctuatie = ".,!?-"
k_ch = k_CH = k_punctuatie = 0
# nr aparitii fiecare semn din sirul punctuatie (fiecare poate sa apara de mai multe ori)
for x in punctuatie:
    k_punctuatie += s.count(x)
# eliminare semne de punctuatie, replacing them with spaces
for c in punctuatie:
    s = s.replace(c, " ")

for cuv in s.split():
    for x in cuv:
        if x.isupper():
            k_CH += 1
        else:
            k_ch += 1
print("nr semne de punctuatie:", k_punctuatie,", nr litere mici:", k_ch, ", nr litere mari:", k_CH)

