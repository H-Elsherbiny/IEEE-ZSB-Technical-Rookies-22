_ = input()
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
lst2.sort()

multiples = []
factor = 1
counter = 0

for i in range(len(lst1)):
    multiples.append([])
    
    while True:
        num = factor * lst1[i]
        
        if num > lst2[0]:
            factor = 1
            break
        
        multiples[i].append(factor * lst1[i])
        factor += 1
        
if len(lst1) != 1:        
    for i in range(len(multiples) - 1):
        mutual_multiples = set(multiples[i]) & set(multiples[i + 1])

else:
    mutual_multiples = multiples[0]
        
for i in mutual_multiples:
    for j in lst2:
        if j % i != 0:
            break
        
    else:
        counter += 1
            
print(counter)        