_ = input()
lst = sorted(list(map(int, input().split())))

temp = 1
counter = 0
num = lst[0]

for i in range(1, len(lst)):
    if lst[i] == num:
        temp += 1
        
    if lst[i] != num or i == len(lst) - 1:
        counter += temp // 2
        num = lst[i]
        temp = 1
        
print(counter)        