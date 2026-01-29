letterFrequency = [
    ('Z', 0.1),
    ('Q', 0.1),
    ('X', 0.2),
    ('J', 0.2),
    ('K', 0.8),
    ('V', 1.0),
    ('B', 1.5),
    ('P', 1.9),
    ('Y', 2.0),
    ('G', 2.0),
    ('F', 2.2),
    ('W', 2.4),
    ('M', 2.4),
    ('U', 2.8),
    ('C', 2.8),
    ('D', 4.3),
    ('L', 4.0),
    ('R', 6.0),
    ('H', 6.1),
    ('S', 6.3),
    ('N', 6.7),
    ('I', 7.0),
    ('O', 7.5),
    ('A', 8.2),
    ('T', 9.1),
    ('E', 12.7)
]

cipherText = "UZQSOVUOHXMOPVGPOZPEVSGZWSZOPFPESXUDBMETSXAIZVUEPHZHMDZSHZOWSFPAPPDTSVPQUZWYMXUZUHSXEPYEPOPDZSZUFPOMBZWPFUPZHMDJUDTMOHMQ"

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cipherFrequency = []

for i in alphabet:
    count = 0
    for j in cipherText:
        if j == i:
            count += 1
    cipherFrequency.append((i, count))

cipherFrequency.sort(key=lambda tup:tup[1])

mostCommon = (cipherFrequency[::-1])

for i in mostCommon[:3]:
    potentialLetter = i[0]
    potentialNumber = ord(potentialLetter)

    pOffset = potentialNumber - ord("E")

    plainText = ""

    for j in cipherText:
        newNumber = ord(j) + pOffset

        if newNumber > 89:
            newNumber -= 26

        if newNumber < 65:
            newNumber += 26

        plainText += chr(newNumber)

    print(plainText, "\n")

for i in mostCommon[:3]:
    potentialLetter = i[0]
    potentialNumber = ord(potentialLetter)

    pOffset = potentialNumber - ord("T")

    plainText = ""

    for j in cipherText:
        newNumber = ord(j) + pOffset

        if newNumber > 89:
            newNumber -= 26

        if newNumber < 65:
            newNumber += 26

        plainText += chr(newNumber)

    print(plainText, "\n")

print(ord("A"), ord("Z"))

    

