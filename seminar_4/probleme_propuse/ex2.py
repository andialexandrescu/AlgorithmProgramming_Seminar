#a)
def lista_pozitii(colectie, proprietate):
    L_pozitii = []
    for poz in range(len(colectie)):
        if proprietate(colectie[poz]) == True:
            L_pozitii.append(poz)
    return L_pozitii
#b)
def este_strict_pozitiv(x):
    return x > 0

t = (1, -2, 3, -4, 5, 6)
print(lista_pozitii(t, este_strict_pozitiv))
def este_semn_punctuatie(x):
    return not(x.isalnum()) and not(x.isspace())

s = "asadar, v-ati saturat?!"
print(lista_pozitii(s, este_semn_punctuatie))
def este_anagrama(cuvant, s):
    return sorted(cuvant) == sorted(s)

text = "listen to the silent voices you've ignored each time your heart used to ache because of her"# compozitie proprie si personala
L_cuv = [cuv for cuv in text.split()]
print(lista_pozitii(L_cuv, lambda x: este_anagrama(x, "silent")))
print(lista_pozitii(L_cuv, lambda x: este_anagrama(x, "each")))
def este_suma_cifre_egala(x, n, s):
    return len(str(x)) == n and sum(int(cif) for cif in str(x)) == s

l_nr = [123, 116, 789, 1091, 222, 303]
print(lista_pozitii(l_nr, lambda x: este_suma_cifre_egala(x, 3, 6)))
