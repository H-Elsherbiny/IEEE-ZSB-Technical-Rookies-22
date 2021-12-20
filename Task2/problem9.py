while True:
    num = int(input("Enter the order of the matrix: "))
    if num > 1:
        break
print("Enter elements : ")
 
test = 1
matrix = []
main_diagonal = secondary_diagonal = 0

while test > 0:
    
    for i in range(num):
        lst = list(map(int, (input().split())))
        matrix.append(lst)
        
    for i in range(num):
        
        main_diagonal += matrix[i][i]
        secondary_diagonal += matrix[num - i - 1][i]
        
        for j in range(num):
            if -100 > matrix[i][j] or matrix[i][j] > 100:
                print("Enter valid elements between [-100, 100]: ")
                break
        else:
            continue
            
        break
    else:
        test = 0

difference = abs(main_diagonal - secondary_diagonal)
print(f"\nThe absolute difference between the sums of its diagonals: {difference}")