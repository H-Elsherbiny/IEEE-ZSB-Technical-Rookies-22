lst = list(map(int,input("Enter a list: ").split()))

for i in range(1, len(lst)):
    key = lst[i]
    
    for j in range(i - 1, -1, -1):    
        if key < lst[j]:
            lst[j + 1] = lst[j]
            lst[j] = key
            
print("Sorted: ", end="")
print(*lst)