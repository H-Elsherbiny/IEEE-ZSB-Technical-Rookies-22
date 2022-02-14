n = int(input().strip())
grid = []

for _ in range(n):
    grid_item = input()
    grid.append(grid_item)
    
temp = grid.copy()
item = [-1, 1]

for i in range(1, n - 1):
    for j in range(1, n - 1):
        status = True
        
        for m in item:
            if grid[i][j] <= grid[i + m][j]:
                status = False
                break
        
        if not status:
            continue
        
        for m in item:
            if grid[i][j] <= grid[i][j + m]:
                status = False
                break
            
        if status:
            temp[i] = temp[i][:j] + 'X' + temp[i][j + 1:]
            
print(*temp, sep=('\n'))