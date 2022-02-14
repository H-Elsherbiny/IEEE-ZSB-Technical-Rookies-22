def ChocolateAndWrappers(chocolate,wrappers,cost):
    if wrappers // cost == 0:
        return chocolate
    
    chocolate += wrappers // cost
    wrappers = wrappers // cost + wrappers % cost
    return ChocolateAndWrappers(chocolate, wrappers, cost)

t = int(input())
lst = []

for _ in range(t):
    
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    c = int(first_multiple_input[1])
    m = int(first_multiple_input[2])

    chocolate = wrappers = n // c
    lst.append(ChocolateAndWrappers(chocolate, wrappers, m))
    
print(*lst, sep=("\n"))