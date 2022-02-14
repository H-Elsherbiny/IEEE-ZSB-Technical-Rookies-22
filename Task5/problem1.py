def max_heap(arr, i, n):
    left = 2 * i + 1
    right = 2 * i + 2
    upper = i
    if left < n and arr[left] > arr[i]:
        upper = left
    if right < n and arr[right] > arr[upper]:
        upper = right
    if upper != i:
        arr[i], arr[upper] = (arr[upper], arr[i])
        max_heap(arr, upper, n)

lst = list(map(int, input().split()))

for i in range(int(len(lst) - 2)//2, -1, -1):
    max_heap(lst, i, len(lst))

print(*lst, sep=(" "))