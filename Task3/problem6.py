num = input()

N = 6174
counter = 0

while num != N:
    # Convert num into a list
    lst = [x for x in str(num)]
    
    if len(str(num)) == 4:
        # Sort lists ascending and descending
        lst1 = sorted(lst, reverse = True)
        lst2 = sorted(lst,)
        
        # Convert lists to integers
        num1 = int("".join(lst1))
        num2 = int("".join(lst2))
        
        num = num1 - num2
        counter += 1
        
    # Make sure the num is 4 digits    
    else:
        num *= 10
        
print(counter)