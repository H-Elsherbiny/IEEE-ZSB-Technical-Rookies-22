first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
d = int(first_multiple_input[1])

arr = list(map(int, input().rstrip().split()))

counter = 0

for i in range(n - 1):
    point = arr[i]
    temp = 1
    
    for j in range(i + 1, n):
        if arr[j] - point == d:
            temp += 1
            point = arr[j]
            
        if temp == 3:
            counter += 1
            temp = 1
            break
        
print(counter)