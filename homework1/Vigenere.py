def encrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
       >>> encrypt_vigenere("PYTHON", "A")
       'PYTHON'
       >>> encrypt_vigenere("python", "a")
       'python'
       >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
       'LXFOPVEFRNHR'
       """


    ciphertext2=""
    Length=len(ciphertext)
    Length2=len(keyword)
    j=0
    for i in range(Length):
        if j==Length2:
              j=0

        x=ord(ciphertext[i])
        if (x>64 and x<123):
            if (x<91):
                if ord(keyword[j])<91:
                    y=ord(keyword[j])-65
                else:
                    y=ord(keyword[j])-97
                Letter=x+y
                if (Letter>90 and Letter<117):
                    Letter=Letter-26
            else:
                if ord(keyword[j])<91:
                    y=ord(keyword[j])-65
                else:
                    y=ord(keyword[j])-97
                Letter=x+y
                if Letter>122:
                    Letter=Letter-26
            y=chr(Letter)

            ciphertext2=ciphertext2 + y



            j=j+1




    ciphertext=ciphertext2
    print(ciphertext)




    return ciphertext

encrypt_vigenere("PYTHON", "A")
encrypt_vigenere("python", "a")
encrypt_vigenere("ATTACKATDAWN", "LEMON")


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:

    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """


    ciphertext2=""
    Length=len(ciphertext)
    Length2=len(keyword)
    j=0
    for i in range(Length):
        if j==Length2:
            j=0

        x=ord(ciphertext[i])
        if (x>64 and x<123):
            if (x<91):
                if ord(keyword[j])<91:
                    y=ord(keyword[j])-65
                else:
                    y=ord(keyword[j])-97
                Letter=x-y
                if (Letter<65):
                    Letter=Letter+26
            else:
                if ord(keyword[j])<91:
                    y=ord(keyword[j])-65
                else:
                    y=ord(keyword[j])-97
                Letter=x-y
                if Letter<91:
                    Letter=Letter+26
            y=chr(Letter)

            ciphertext2=ciphertext2 + y



            j=j+1




    ciphertext=ciphertext2
    print(ciphertext)

    return ciphertext
decrypt_vigenere("PYTHON", "A")
decrypt_vigenere("python", "a")
decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
