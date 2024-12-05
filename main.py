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

def generatePassword():
    password = ""
    for i in range(14):
        password = password + random.choice(characters)
    return password

for i in range(howManyPasswords):
    print(generatePassword())
    passwordsFile.write(f'{generatePassword()}\n')


passwordsFile.close()


