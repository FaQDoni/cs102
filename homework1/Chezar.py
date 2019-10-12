def encrypt_caesar(plaintext: str) -> str:

	for i in plaintext:

		x=ord(i)
		if (x>64 and x<123):
			if (x>87 and x<91) or (x<123 and x>119):
				x=x-26
			y=chr(x+3)
			plaintext=plaintext.replace(i, y)
	print(plaintext)
	return plaintext


def decrypt_caesar(ciphertext: str) -> str:

	for i in ciphertext:

		x=ord(i)
		if (x>64 and x<123):
			if (x<68 and x<91) or (x<100 and x>96):
				x=x+26
			y=chr(x-3)
			ciphertext=ciphertext.replace(i, y)
	print(ciphertext)
	return ciphertext

encrypt_caesar("PYTHON")
encrypt_caesar("python")
encrypt_caesar("Python3.8")
decrypt_caesar("SBWKRQ")
decrypt_caesar("sbwkrq")
decrypt_caesar("Sbwkrq3.8")