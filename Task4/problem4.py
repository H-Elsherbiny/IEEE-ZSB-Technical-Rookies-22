first_multiple_input = input().rstrip().split()
d1 = int(first_multiple_input[0])
m1 = int(first_multiple_input[1])
y1 = int(first_multiple_input[2])

second_multiple_input = input().rstrip().split()
d2 = int(second_multiple_input[0])
m2 = int(second_multiple_input[1])
y2 = int(second_multiple_input[2])


sum1 = d1 + m1 * 30 + y1 * 365
sum2 = d2 + m2 *30 + y2 * 365

if sum2 > sum1:
    print(0)
    
elif y1 > y2:
    print(10000 * (y1 - y2))
    
elif m1 > m2:
    print(500 * (m1 - m2))

else:
    print(15 * (d1 - d2))