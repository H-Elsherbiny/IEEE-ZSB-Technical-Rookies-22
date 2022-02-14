t = int(input())

for _ in range(t):
    first = input()
    second = input()
    
    diff = len(first) - len(second)
    
    for i in first:
        if i in second:
            second = second[:second.index(i)] + second[second.index(i) + 1:]
            
    print(2 * len(second) + diff)