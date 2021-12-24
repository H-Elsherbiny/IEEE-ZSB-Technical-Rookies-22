_ = input()
lst = sorted(list(map(int, input().split())))

counter = temp = 1
num = most = lst[0]

for i in range(1, len(lst)):
    if lst[i] == num:
        temp += 1
    if lst[i] != num or i == len(lst) - 1:
        if temp > counter:
            counter = temp
            most = lst[i - 1]
            
        num = lst[i]
        temp = 1
print(most)        