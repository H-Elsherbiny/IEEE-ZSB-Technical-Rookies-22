from random import randint

counter = 1
y = 0

x = randint(1, 10)

while True:
    y = int(input("Guess a number: "))
    if y != x:
        print("Wrong guess")
        counter += 1

    else:
        break

print(f"Yay you got it {counter} tries")