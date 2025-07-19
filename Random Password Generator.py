import random
import string

all_symbols = string.ascii_letters + str(string.digits) + string.punctuation

password = ""

pass_length = int(input("What is length of the password You want: "))

for _ in range(101):
    password += all_symbols[random.randint(0, len(all_symbols)-1)]

print(password[:pass_length+1])
    

