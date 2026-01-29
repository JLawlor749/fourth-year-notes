# Written by James Lawlor, C22388703
# Updated 07/10/2025
# Advanced Security Assignment 1
# This program implement the three ciphers, Ceaser, Vigenere, and Hill, in Python.
# It uses the numpy library for matrix operations.

import numpy as np


def Ceaser(text, mode, key):
    newString = ""
    
    # Encrypt
    if mode == 1:
        for el in text:

            # If the character is a capital or lowercase letter.
            if (ord(el) > 96 and ord(el) < 123) or (ord(el) > 64 and ord(el) < 91):

                # Adding the key to the letter's position.
                newIndex = ord(el) + key

                # If the key would make it fall outside the range of being a letter, it loops around.
                if el.isupper():
                    while newIndex > 90:
                        newIndex = (newIndex - 90) + 64
                else:
                    while newIndex > 122:
                        newIndex = (newIndex - 122) + 96

                newString += chr(newIndex)

            else:
                newString += el
            
    # Decrypt
    if mode == 2:
        for el in text:

            # If the character is a capital or lowercase letter.
            if (ord(el) > 96 and ord(el) < 123) or (ord(el) > 64 and ord(el) < 91):

                # Subtracting the key from the letter's position.
                newIndex = ord(el) - key

                # If the key would make it fall outside the range of being a letter, it loops around.
                if el.isupper():
                    while newIndex < 65:
                        newIndex = 91 - (65 - newIndex)
                else:
                    while newIndex < 97:
                        newIndex = 123 - (97 - newIndex)

                newString += chr(newIndex)

            else:
                newString += el

    return newString

def Vignere(text, mode, key):
    newString = ""
    
    # Encrypt
    if mode == 1:
        el = 0
        co = 0
        while el in range(len(text)):

            # If the element is not an uppercase or lowercase letter, add it to the new string and increment the counter.
            if not ((ord(text[el]) > 96 and ord(text[el]) < 123) or (ord(text[el]) > 64 and ord(text[el]) < 91)):
                newString += text[el]
                el += 1
                continue

            # Otherwise, get the position in the alphabet of the current element of the key. Then add this to the current string element, and loop if it goes over the bounds.
            else:
                if text[el].isupper():
                    currentIndex = ord(text[el])
                    indexDiff = ord(key[co]) - 97
                    newIndex = currentIndex + indexDiff
                    while newIndex > 90:
                        newIndex = 64 + (newIndex-90)

                else:
                    currentIndex = ord(text[el])
                    indexDiff = ord(key[co]) - 97
                    newIndex = currentIndex + indexDiff
                    while newIndex > 122:
                        newIndex = 96 + (newIndex-122)

                newString += chr(newIndex)

            # Increment the seperate counters for the string, and for the key.
            el += 1    
            co += 1
            
    # Decrypt
    if mode == 2:
        el = 0
        co = 0
        while el in range(len(text)):

            # If the element is not an uppercase or lowercase letter, add it to the new string and increment the counter.
            if not ((ord(text[el]) > 96 and ord(text[el]) < 123) or (ord(text[el]) > 64 and ord(text[el]) < 91)):
                newString += text[el]
                el += 1
                continue

            # Otherwise, get the position in the alphabet of the current element of the key. Then subtract this from the current string element, and loop if it goes over the bounds.
            else:
                if text[el].isupper():
                    currentIndex = ord(text[el])
                    indexDiff = ord(key[co]) - 97
                    newIndex = currentIndex - indexDiff
                    while newIndex < 65:
                        newIndex = 91 - (65-newIndex)

                else:
                    currentIndex = ord(text[el])
                    indexDiff = ord(key[co]) - 97
                    newIndex = currentIndex - indexDiff
                    while newIndex < 97:
                        newIndex = 123 - (97-newIndex)

                newString += chr(newIndex)

            # Increment the seperate counters for the string, and for the key.
            el += 1
            co += 1

    return newString

def Hill(text, mode, key):

    # Encrypt
    if mode == 1:
        text = text.upper()
        textAsNumbers = []

        text = text.replace(" ", "")

        # Convert each letter in the string to a number.
        for i in text:
            textAsNumbers.append(ord(i)-65)

        digraphs = []


        for i in range(len(textAsNumbers)):
            if i%2 == 0:
                try:
                    digraphs.append([textAsNumbers[i], textAsNumbers[i+1]])
                except IndexError:
                    digraphs.append([textAsNumbers[i], 0])

        key = key.upper()
        numKey = []

        # Convert the key to integers.
        for i in key: 
            numKey.append(ord(i)-65)

        # Turn the four letter word into a 2x2 matrix.
        keyMatrix = [[numKey[0], numKey[1]], [numKey[2], numKey[3]]]

        keyMatrix = np.array(keyMatrix)

        # Use numpy to get the dot products of the key and each string vector.
        encrypted = []

        for i in range(len(digraphs)):
            encrypted.append(np.dot(keyMatrix, digraphs[i]))

        encrypted = np.array(encrypted)

        # Flatten the array back down into a vector.
        encrypted = np.matrix.flatten(encrypted)

        newString = ""

        # Convert the new dot product vector back into a string.
        for i in encrypted:
            newString += chr((i % 26 ) + 65)

        return newString

    # Decrypt
    if mode == 2:
        text = text.upper()
        textAsNumbers = []

        text = text.replace(" ", "")

        # Convert each letter in the string to a number.
        for i in text:
            textAsNumbers.append(ord(i)-65)

        digraphs = []


        for i in range(len(textAsNumbers)):
            if i%2 == 0:
                try:
                    digraphs.append([textAsNumbers[i], textAsNumbers[i+1]])
                except IndexError:
                    digraphs.append([textAsNumbers[i], 0])

        key = key.upper()
        numKey = []

        # Convert the key to integers.
        for i in key: 
            numKey.append(ord(i)-65)
        
        keyMatrix = [[numKey[0], numKey[1]], [numKey[2], numKey[3]]]

        # I learned that the built-in function to invert a matrix is no good with mod 26, it has to be done manually.
        determinant = int(round(np.linalg.det(keyMatrix))) % 26

        inverse = 0

        for i in range(1, 26):
            if (determinant * i) % 26 == 1:
                inverse = i

        # Turn the four letter word into the adjugate matrix.
        adjMatrix = np.array([[keyMatrix[1][1], -keyMatrix[0][1]], [-keyMatrix[1][0], keyMatrix[0][0]]])

        keyMatrix = (inverse * adjMatrix) % 26

        keyMatrix = np.array(keyMatrix)

        # Use numpy to get the dot products of the key and each string vector.
        encrypted = []

        for i in range(len(digraphs)):
            encrypted.append(np.dot(keyMatrix, digraphs[i]) % 26)

        encrypted = np.array(encrypted)

        # Flatten the array back down into a vector.
        encrypted = np.matrix.flatten(encrypted)

        newString = ""

        # Convert the new dot product vector back into a string.
        for i in encrypted:
            newString += chr((i % 26 ) + 65)

        return newString







endProgram = False

# Simple while loop menu system.
while endProgram == False:
    print("~~~~~ Decryption and Encryption ~~~~~\n")
    print("Please select an operation:")
    print("1. Encrypt\n2. Decrypt\n3. Exit")
    selection = int(input())

    print()

    # Gets input to decide whether to encrypt or decrypt.
    if selection == 1:
        print("Which cipher would you like to use?")
        print("1. Ceaser\n2. Vignere\n3. Hill")
        cipher = int(input())

        print()

        # Then it asks which algorithm you want to use and gets your plaintext and key accordingly.
        if cipher == 1:
            print("Enter your plaintext:")
            plainText = input()

            print("\nEnter your key:")
            key = int(input())

            print("\nEncrypted text:")
            print(Ceaser(plainText, selection, key))

        if cipher == 2:
            print("Enter your plaintext:")
            plainText = input()

            print("\nEnter your key word:")
            key = input()
            key = key.lower()

            # For Vigenere, repeat the key if it isn't long enough by appending it to itself.
            while len(key) < len(plainText):
                key = key + key

            print("\nEncrypted text:")
            print(Vignere(plainText, selection, key))

        if cipher == 3:
            print("Enter your plaintext:")            
            plainText = input()

            print("Enter a four-letter key word:")            
            key = input()

            # For a 2x2 Hill Cipher, the key must be 4 letters.
            if len(key) != 4:
                raise ValueError("Key must be 4 letters long.")

            print(Hill(plainText, selection, key))


    elif selection == 2:
        print("Which cipher would you like to decrypt?")
        print("1. Ceaser\n2. Vignere\n3. Hill")
        cipher = int(input())

        print()

        # Then it asks which algorithm you want to use and gets your plaintext and key accordingly.
        if cipher == 1:
            print("Enter your ciphertext:")
            cipherText = input()

            print("\nEnter your key:")
            key = int(input())

            print("\nDecrypted text:")
            print(Ceaser(cipherText, selection, key))

        if cipher == 2:
            print("Enter your ciphertext:")
            cipherText = input()

            print("\nEnter your key word:")
            key = input()

            # For Vigenere, repeat the key if it isn't long enough by appending it to itself.
            while len(key) < len(cipherText):
                key = key + key

            print("\nDecrypted text:")
            print(Vignere(cipherText, selection, key))

        if cipher == 3:
            print("Enter your ciphertext:")            
            plainText = input()

            print("Enter a four-letter key word:")            
            key = input()

            # For a 2x2 Hill Cipher, the key must be 4 letters.
            if len(key) != 4:
                raise ValueError("Key must be 4 letters long.")

            print(Hill(plainText, selection, key))

    elif selection == 3:
        print("\n\nGoodbye!!!")
        endProgram = True

    else:
         print("Invalid selection!!!")

    print("\n\n")