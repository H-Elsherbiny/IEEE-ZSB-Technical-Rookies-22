lst = [0 , 1]

num = int(input("Enter a number: "))

for i in range(num - 2):
    lst.append(lst[i] + lst[i + 1])

if num == 1:
    print(lst[0])

else:
    print(*lst)