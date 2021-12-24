_ = input()
lst = list(map(int, input().split()))

minimum = maximum = lst[0]
min_count = max_count = 0

for i in range(1, len(lst)):
    if lst[i] > maximum:
        max_count += 1
        maximum = lst[i]
    
    elif lst[i] < minimum:
        min_count += 1
        minimum = lst[i]
        
print(max_count, min_count)        