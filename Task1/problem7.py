x = 0
sum0 = 0

while x < 1:
    x = int(input("Enter a positive number: "))

for i in range(x + 1):
    if i % 3 == 0 or i % 5 == 0:
        sum0 += i
        
print(f"sum = {sum0}") 