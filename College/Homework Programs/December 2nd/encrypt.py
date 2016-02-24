def encrypt(plaintext):
	encryptedChars = []

	for i in plaintext:
		encrypted = chr(ord(i) + 1)
		encryptedChars.append(encrypted)

	ciphertext = "".join(encryptedChars)
	return ciphertext

p = str(input("Enter the plaintext you want to encrypt: "))
print(encrypt(p))