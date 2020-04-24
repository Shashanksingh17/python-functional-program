rows = int(input("Enter Row: "))
columns = int(input("Enter Coloumn: "))

# Initialize matrix
matrix = []
print("Enter the array:")
# For user input
for i in range(rows):  # A for loop for row entries
    a = []
    for j in range(columns):  # A for loop for column entries
        a.append(int(input()))
    matrix.append(a)

# For printing the matrix
for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end=" ")
    print()