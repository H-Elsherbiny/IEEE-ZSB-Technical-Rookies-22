from random import randint

N = 3
counter = 1
count_hit = 0
count_miss = 0

num = temp = str(randint(100,999))


while True:
    guess = input(f"Guess {N}-digit numbers: ")
    
    for i in range(N):
        if guess[i] == num[i]:
            count_hit += 1
            temp = temp.replace(temp[i], " ")
            
    for i in range(N):
        if guess[i] in temp:
            count_miss += 1
    
    if guess == num:
        print(f"Yay you got it {counter} tries!")
        break
    
    else:
        counter += 1
        print(f"{count_hit} hit(s), {count_miss} miss(es)")
        count_hit = count_miss = 0