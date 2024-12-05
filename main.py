import django
import string  
import random
letters = list(string.ascii_letters)
digits = list(string.digits)
punctuation = ["!", "@", "#", "$", "%", "^", "&", "*"]

characters = letters + digits + punctuation


howManyPasswords = int(input("Enter how many passwords to generate?: "))
passwordsFileName = input("Name the file to output passwords (default: passwords.txt): ")
if passwordsFileName == "":
    passwordsFile = passwordsFile = open("passwords.txt", "a")
else:
    passwordsFile = open(f"{passwordsFileName}.txt", "a")

for r in range(howManyPasswords):
    password = ""
    while len(password) != 14:
        for i in range(len(characters)):
            randomChar = random.randint(1, len(characters))

            if i == randomChar:
                password = password + characters[i]
                

    print(password)
    passwordsFile.write(f'{password}\n')


passwordsFile.close()


