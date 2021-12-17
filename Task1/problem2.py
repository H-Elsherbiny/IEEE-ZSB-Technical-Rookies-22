lst = [2]

while True:
    num = int(input("Enter a number: "))
    if num > 1:
        break

for i in range(2, num + 1):
    for j in range(2, i):
        if i % j == 0:
            break

        elif j == i - 1:
            lst.append(i)

print(*lst)