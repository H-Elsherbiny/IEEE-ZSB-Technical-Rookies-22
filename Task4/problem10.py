bnm = input().split()
b = int(bnm[0])
n = int(bnm[1])
m = int(bnm[2])

keyboards = list(map(int, input().rstrip().split()))
drives = list(map(int, input().rstrip().split()))

result = -1

for i in keyboards:
    for j in drives:
        if i + j <= b and i + j > result:
            result = i + j
                
print(result)