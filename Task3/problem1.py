bottles = []
sum_remaining = 0

num = int(input())

for i in range(num):
    bottles.append([])
    bottles[i] = (list(map(int, input().split()))) 
    
bottles.sort(key = lambda x: x[1])
volume = bottles[-1][1] + bottles[-2][1]

for i in range(num):
    sum_remaining += bottles[i][0]
        
if sum_remaining > volume:
    print("\nNo")
    
else:
    print("\nYes")    