string = "hackerrank"

t = int(input())

for _ in range(t):
    s = input()    
    j = -1
    counter = 0

    for i in string:
        temp = j + 1
        for j in range(temp, len(s)):
            if i == s[j]:
                counter += 1
                break

    if counter == 10:
        print("YES")
    else:
        print("NO")