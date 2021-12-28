from random import randint

N = 3
counter = 1
count_hit = 0
count_miss = 0

num = randint(10 ** (N - 1) , 10 ** N - 1)
num = [int(i) for i in str(num)]

while True:
    guess = input(f"Guess {N}-digit numbers: ")
    guess = [int(i) for i in guess]
    
    for i in range(N):
        if guess[i] == num[i]:
            count_hit += 1
            guess[i] = None
        
    for i in num:
        if i in guess:
            count_miss += 1
            guess[guess.index(i)] = None
    
    if count_hit == N:
        print(f"Yay you got it {counter} tries!")
        break
    
    else:
        counter += 1
        print(f"{count_hit} hit(s), {count_miss} miss(es)")
        count_hit = count_miss = 0