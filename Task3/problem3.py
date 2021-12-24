import random
import string

N = 10
temp = ""

numbers = string.digits
sympoles = ['@', '#', '$', '%', '&']
characters = string.ascii_letters + string.digits + string.punctuation

temp += random.choice(numbers)
temp += random.choice(sympoles)

for i in range(N - 2):
    temp += random.choice(characters)
    
password = random.sample(temp, len(temp))    
print(*password, sep = '')    