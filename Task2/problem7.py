while True:
    org = input("Enter a string about [1, 200] characters: ")
    if 1 <= len(org) <= 200:
        break

sub = input("Enter substring: ")

count = 0

for i in range(len(org) - len(sub) + 1):
    if org[i : i + len(sub)] == sub:
        count += 1
        
print(count)        