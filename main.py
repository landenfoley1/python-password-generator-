import string
import random

x = int(input("how many digits do you want your password: "))
y = str(input("type letters, numbers, both or everything for the password type:  "))

letters = string.ascii_letters
numbers = "0123456789"
symbols = "!@#$%&"

characters = letters + numbers + symbols
words = letters 
number = numbers
symbol = symbols
both = letters + numbers

password = ""
if(y == "letters"):
    for i in range(x):
        password += random.choice(words)
    print(f"Your new password is: {password}")
elif(y == "numbers"):
    for i in range(x):
        password += random.choice(number)
    print(f"Your new password is: {password}")
elif(y == "both"):
    for i in range(x):
        password += random.choice(both)
    print(f"Your new password is: {password}")

else:
    for i in range(x):
        password += random.choice(characters)
    print(f"Your new password is: {password}")




