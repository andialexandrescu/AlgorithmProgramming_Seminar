'''Implementați cifrul lui Cezar (https://ro.wikipedia.org/wiki/Cifrul_Cezar) pentru a cripta/decripta o propoziție citită de la tastatură.'''
message = input("message=")
key = int(input("key="))  # Convert the key to an integer
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result_encrypt = ""
result_decrypt = ""

# Encryption
for letter in message:
    if letter in alpha:
        # Find the corresponding ciphertext letter in the alphabet
        letter_index = (alpha.find(letter) + key) % len(alpha)
        result_encrypt = result_encrypt + alpha[letter_index]
    else:
        result_encrypt = result_encrypt + letter

print("Encryption result:", result_encrypt)

# Decryption
for letter in message:  # Decrypt the encrypted message
    if letter in alpha:
        letter_index = (alpha.find(letter) - key) % len(alpha)
        result_decrypt = result_decrypt + alpha[letter_index]
    else:
        result_decrypt = result_decrypt + letter

print("Decryption result:", result_decrypt)

