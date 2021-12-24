_ = input()
steps = input()

old_level = 0
current_level = 0
counter = 0

for i in range(len(steps)):
    old_level = current_level
    if steps[i] =='D':
        current_level -= 1
        
    else:
        current_level += 1
        
    if old_level == 0 and current_level < 0:
        counter += 1
        
print(counter)        