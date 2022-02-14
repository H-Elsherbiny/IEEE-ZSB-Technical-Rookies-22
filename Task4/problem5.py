def findDigits(n):
    counter = 0
    for i in range(len(n)):
        try:
            if int(n) % int(n[i]) == 0:
                counter += 1
        
        except:
            i += 1
            
    return counter

lst = []
t = int(input())

for _ in range(t):
    lst.append(findDigits(input()))

print(*lst, sep=("\n"))