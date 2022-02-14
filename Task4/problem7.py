from math import ceil

start = int(input())
end = int(input())
test = False

for num in range(start, end + 1):
    result = '0' + str(num ** 2)
    left = result[:ceil(len(result) / 2)]
    right = result[ceil(len(result) / 2):]
    
    if int(left) + int(right) == num:
        print(num, end=(" "))
        test = True
        
if not test:
    print("INVALID RANGE")