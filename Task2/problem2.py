lst = list(input("Enter a sorted list: ").split())

print(*sorted(set(lst)))