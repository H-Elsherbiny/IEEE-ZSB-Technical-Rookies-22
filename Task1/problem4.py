list1 = []
list1_long = []

list1 = input("Enter the sentence: ").split()

for i in range(len(list1)):
    list1_long.append(len(list1[i]))

longest = max(list1_long) + 4

print("*" * longest)

for i in range(len(list1)):
    print("*" + " " + list1[i] + " " * (longest - 3 - len(list1[i])) + "*")

print("*" * longest)