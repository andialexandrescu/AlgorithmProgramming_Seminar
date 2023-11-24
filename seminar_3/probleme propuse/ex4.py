'''Fișierul text numere.txt conține numere naturale pe mai multe linii, numerele fiind despărțite între ele prin spații. Scrieți un program care să afișeze cel mai mare și cel mai mic număr care se poate obține din toate cifrele tuturor numerelor din fișier. Rezolvați problema în cel puțin 3 moduri diferite, respectiv folosind șiruri de caractere, liste, mulțimi și dicționare!'''

try:
    f = open("numere.txt")
    valori = f.read().split()
    f.close()
except FileNotFoundError:
    print("Fisier inexistent!")
    exit(0)

#a) prima varianta cu string
concat_str = "".join(str(cif) for cif in valori)
cifre = [int(cif) for cif in concat_str]

max_number_str = ''.join(map(str, sorted(cifre, reverse=True)))

min_cif = min(int(cif) for cif in concat_str if cif != '0')
cifre.remove(min_cif)
min_number_str = str(min_cif) + ''.join(map(str, sorted(cifre)))

print(f"Minim (var str): {min_number_str}")
print(f"Maxim (var str): {max_number_str}")

#b) a doua varianta cu lists
concat_str = "".join(str(cif) for cif in valori)
cifre = [int(cif) for cif in concat_str]

max_number_list = sorted(cifre, reverse=True)

min_cif = min(int(cif) for cif in concat_str if cif != '0')
cifre.remove(min_cif)
min_number_list = [min_cif] + sorted(cifre)

print(f"Minim (var lists): {''.join(map(str, min_number_list))}")
print(f"Maxim (var lists): {''.join(map(str, max_number_list))}")

#c) a treia varianta cu dictionare GRESIT DE CORECTAT
concat_str = "".join(str(cif) for cif in valori)
cifre = [int(cif) for cif in concat_str]
print(set(concat_str))
d = {}
for cif in set(concat_str):
    val = cifre.count(cif)
    d[cif] = val
print(d)

max_number_dict = sorted(cifre, reverse=True)

