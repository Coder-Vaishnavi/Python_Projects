import secrets
import string
import random

length=int(input("Enter the Length:"))

letters = string.ascii_letters

digits = string.digits

special_chars = string.punctuation

password = " "
for i in range(length):
    next_character=random.choice(letters+digits+special_chars)
    password+= next_character
print(password)
