import math

text = input()
num = int(input())
counter = 0

index = math.ceil(num / len(text))
temp = text * index

for i in range(num):
    if temp[i] == 'r':
        counter += 1
        
print(counter)        