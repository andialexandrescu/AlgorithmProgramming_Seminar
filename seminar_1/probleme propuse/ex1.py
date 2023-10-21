'''Se citește un șir format din numere naturale cu proprietatea că fiecare valoare distinctă
din șir apare de un număr par de ori, mai puțin una care apare de un număr impar de ori.
Să se afișeze valoarea care apare de un număr impar de ori în șirul dat'''

n = int(input("n="))
x_xor_y = 0
for i in range(1, n+1):
    x = int(input("x="))
    x_xor_y = x_xor_y ^ x
print(x_xor_y)

'''problema consta in folosirea operatorului xor, iar stiind faptul ca 
x^x=0 iar x^0=x rezulta ca putem citi toate nr din sirul de n termeni
si sa le calculam val xor rezultata. aparitia unei valori
de un nr par de ori inseamna 0 compus cu un a, el fiind termenul cautat
(chiar daca a apare de un nr impar de ori x_xor_y va deveni 0^a = a, 
de exemplu (a^a)^a=0^a=a)'''