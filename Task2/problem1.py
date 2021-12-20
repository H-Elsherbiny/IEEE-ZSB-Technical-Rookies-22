word = input("Enter a word: ")
end = int(len(word) / 2 - 1)

for i in range(end):
    if word[i] != word[len(word) - 1 -i]:
        print("No")
        break
    
else:
    print("Yes")    