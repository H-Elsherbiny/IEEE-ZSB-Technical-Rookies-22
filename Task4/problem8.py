def stones(n, a, b):
    first = min(a, b)
    last = max(a, b)
    lst = []
    
    start = first * (n - 1)
    end = last * (n - 1) + 1
    diff = last - first
    
    try:    
        for i in range(start, end, diff):
            lst.append(i)
            
    except:
        lst.append(start)
    
    return lst


time = int(input())
stones_list = []

for _ in range(time):
    n = int(input())
    a = int(input())
    b = int(input())
    
    stones_list.append(stones(n, a, b))
    
for i in range(time):
    print(*stones_list[i], sep=(" "))