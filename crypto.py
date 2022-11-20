"""
Student: Elon Hadad  
Assignment no. 1 
Program: crypto.py 
"""

import random


def is_legal_key(k):
    """return true if the string gets Valid key.
    (26 letters a,z which all lowercase)"""

    lst = []
    for char in k:
        if char.islower() and char not in lst:
            lst.append(char)
    if len(lst) == 26:
        return True


def generate_key():
    """Produces and returns an encryption key"""

    abc = list(map(chr, range(97, 123)))
    random.shuffle(abc)
    key = "".join(str(char) for char in abc)

    return key


def encrypt(s, k):
    """receives a string 's' and an encryption key 'k'
    and returns the string is encrypted by the key 'k'"""

    abc = list(map(chr, range(97, 123)))
    dic = {abc[i]: k[i] for i in range(len(abc))}
    enc = ""
    for char in s:
        if char.isalpha():
            d = char.lower()
            enc += dic.get(d)

    return enc


def decrypt(s, k):
    """receives an encrypted string 's' and an encryption key 'k'
    And returns the string decoded by the key 'k'"""

    abc = list(map(chr, range(97, 123)))
    dic = {k[i]: abc[i] for i in range(len(abc))}
    dec = ""
    for char in s:
        d = char
        dec += dic.get(d)

    return dec


def main():
    while True:
        encrypt_or_decrypt = input('please enter "e" or "d" (encrypt,decrypt): ')
        try:
            if encrypt_or_decrypt == 'e':
                k = generate_key()
                file_1 = open('key.txt', 'w')
                file_1.write(k)
                file_1.close()

                file_2 = open('plaintext.txt', 'r')
                s = file_2.read()
                file_2.close()

                file_3 = open('ciphertext.txt', 'w')
                file_3.write(encrypt(s, k))
                file_3.close()

            elif encrypt_or_decrypt == 'd':
                file_1 = open('key.txt', 'r')
                k = file_1.read()
                file_1.close()

                file_2 = open('ciphertext.txt', 'r')
                s = file_2.read()
                file_2.close()

                if is_legal_key(k):
                    file_3 = open('decrypted.txt', 'w')
                    file_3.write(decrypt(s, k))
                    file_3.close()

                else:
                    print('the key is not legal')

            else:
                if encrypt_or_decrypt != 'd':
                    break

        except IOError:
            print("File note found, make sure that the file is in the project folder")


if __name__ == '__main__':
    main()
