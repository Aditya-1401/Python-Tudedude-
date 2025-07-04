import random
import string

"""print(string.ascii_letters)
print(string.digits)
print(string.punctuation)"""

pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation


"""list comprehension
password = "".join([random.choice(charValues) for i in range(pass_len)])"""



password =""
for i in range(pass_len):
    password += random.choice(charValues)

print("your random password is = ", password) 




