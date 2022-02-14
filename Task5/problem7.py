first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

topic = []
attend = [0] * m

for _ in range(n):
    topic_item = input()
    topic.append(topic_item)

for i in range(n - 1):
    for j in range(i + 1, n):
        temp = bin(int(topic[i], 2) | (int(topic[j], 2))).count("1")
        attend[temp - 1] += 1

        
for i in range(1, m + 1):
    if attend[-i] != 0:
        print(m - i + 1)
        print(attend[-i])
        break