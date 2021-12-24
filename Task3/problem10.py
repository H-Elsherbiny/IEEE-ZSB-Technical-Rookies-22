from math import ceil

num = int(input())
page = int(input())

start = page // 2

if num % 2 == 0:
    end = ceil((num - page) / 2)

else:
    end = (num - page) // 2
    
if end > start:
    print(start)
    
else:
    print(end)