'''Scrieți o funcție care verifică dacă două șiruri de caractere sunt anagrame sau nu utilizând un singur vector de frecvențe.'''
s = input("s=")
t = input("t=")
freq_str = [0] * 26

if len(s) == len(t):
    for i in range(len(s)):
        # increment count by 1 for 1st string
        freq_str[ord(s[i])-ord('a')] += 1
        # decrement count by 1 for 2nd string
        freq_str[ord(t[i]) - ord('a')] -= 1

for x in freq_str:
    if x != 0:
        print("nu sunt anagrame")
        break
else:
    print("da, sunt anagrame")

