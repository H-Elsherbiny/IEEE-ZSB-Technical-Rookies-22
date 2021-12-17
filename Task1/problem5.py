sum1 = sum2 = j = 0

length = int(input("Enter the length of the list: "))
lst = list(map(int, input("Enter the list: ").split()))


for i in range(length):
    sum1 += lst[i]
print(f"sum = {sum1}")


while j < length:
    sum2 += lst[j]
    j += 1
print(f"sum = {sum2}")


def sum3(lst, length):
    if length == 1:
        return lst[0]
    return lst[length - 1] + sum3(lst, length - 1)
    
print(f"sum = {sum3(lst, length)}")