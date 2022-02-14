distance = float('inf')

lst = list(input("Enter a list: ").split())

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j]:
            if j - i < distance:
                distance = j - i
                break
                
                
print(f"The minimume distance = {distance}")