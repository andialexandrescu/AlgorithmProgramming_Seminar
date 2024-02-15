def cauta(n, *s):
    rez = []
    for sir in s:
        if len(sir)==n:
            rez.append(sir)
    return rez
n1 = 5
l_siruri1 = cauta(n1, "apple", "banana", "orange", "kiwi", "grape")
if l_siruri1 == []:
    print(f"Nu exista niciun sir de lungime {n1}")
else:
    print(*l_siruri1, sep="\t")
def cauta_generator(n, *s):
    for sir in s:
        if len(sir)==n:
            yield sir

n2 = 6
l_siruri2 = cauta_generator(n2, "quince", "apple", "banana", "orange", "kiwi", "cherry", "grape")
#print(l_siruri2)# Gresit, va afisa: <generator object cauta_generator at 0x00000192DA8CC9E0>
lst = next(l_siruri2, None)
#print(lst)# Gresit, va printa doar: quince
if l_siruri2 is None:
    print(f"Nu exista niciun sir de lungime {n2}")
else:
    while lst is not None:
        print(lst, end="\t")
        lst = next(l_siruri2, None)

