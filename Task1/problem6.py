x = 0

while x < 1:
    x = int(input("Enter a positive number: "))

def sum0(num):
    if num == 1:
        return 1
    
    return num + sum0(num - 1)
    
print(f"sum = {sum0(x)}")