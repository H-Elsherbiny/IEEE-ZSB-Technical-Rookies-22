first = list(map(int, input().split()))
days = first[0]
time = first[1]

second = list(map(int, input().split()))

for i in range(days):
    time = time - (86400 - second[i])
    if time <= 0:
        print(i + 1)
        break