# I won't even use this :)
while True:
    num = int(input("Enter a number between [2, 10]: "))  
    if 2 <= num <= 10:
        break

test = 1
while test > 0:
    arr = sorted(set(map(int,input("Enter scores between [-100, 100]: ").split())))
    
    for i in range(len(arr)):
        if -100 > arr[i] or arr[i] > 100:
            break
        
    else:
        test = 0        
    

print(f"The runner-up score: {arr[len(arr) - 2]}")