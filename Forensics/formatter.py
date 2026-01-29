myString = ""
finalString = []

print("Enter metadata to be formatted: ")

while myString != "0":
    myString = input()
    finalString .append(myString)


for i in range(len(finalString)):
    if i % 2 == 0:
        try:
            print(finalString[i] + " " + finalString[i+1])
        except IndexError:
            break