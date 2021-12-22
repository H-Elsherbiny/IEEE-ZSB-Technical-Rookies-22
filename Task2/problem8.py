students = []


while True:
    num = int(input("Enter the number of the students [2, 5]: "))
    if 2 <= num <= 5:
        break


# Store the input in nested list
for i in range(num):
    students.append([])
    students[i].append(input("\nStudent name: "))
    students[i].append(float(input("Student grade: ")))


# Sort the nested list by the grade    
students.sort(key = lambda x: x[1])


# Find the second smallest grade index
for i in range(num):
    if students[i][1] - students[0][1] != 0:
        break


names = [students[i][0]]

# Searching for other students with the second smallest grade 
for j in range(i + 1, num):
    if students[j][1] == students[i][1]:
        names.append(students[j][0])
      
print("\n\n")        
print(*sorted(names), sep = "\n")