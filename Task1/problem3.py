lst = list(map(int, input("Enter a sorted list: ").split()))
num = int(input("Enter a number: "))

def binary_search(arr, start, end, number):
    if end >= start:
    
        x = start + (end - start) // 2
        if arr[x] == number:
            return True
        
        elif arr[x] > number:
            return binary_search(arr, start, x - 1, number)
        
        elif arr[x] < number:
            return binary_search(arr, x + 1, end, number)
    
    else:
        return False
        
        
if binary_search(lst, 0, len(lst) - 1, num):
    print("Found!")
    
else:
    print("Not found!")