t = int(input())

for _ in range(t):
    first = list(map(int, input().split()))
    friend = first[0]
    delete = first[1]
    status = False
    
    popularity = list(map(int, input().split()))
    temp = []
    
    for i in popularity:
        
        while delete > 0 and temp and temp[-1] < i:
            temp.pop()
            delete -= 1
            
        temp.append(i)
    print(*temp, sep=(" "))