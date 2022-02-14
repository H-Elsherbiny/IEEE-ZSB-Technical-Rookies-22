ranked_count = int(input().strip())
ranked = list(map(int, input().rstrip().split()))

player_count = int(input().strip())
player = list(map(int, input().rstrip().split()))

temp_ranked = [ranked[0]]

for i in ranked:
    if i == temp_ranked[0]:
        continue
    temp_ranked.insert(0, i)
    

j = 0
for i in player:
    while j < len(temp_ranked) and temp_ranked[j] <= i:
        j += 1
    print(len(temp_ranked) - j + 1)