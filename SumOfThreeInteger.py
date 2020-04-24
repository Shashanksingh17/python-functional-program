size = int(input("Enter the Number Of Element"))
matrix = []
for count in range(size):
    matrix.append(int(input("Enter " + str(count + 1) + " element")))
for i in range(size - 2):
    for j in range(i + 1, size - 1):
        for k in range(j + 1, size):
            if matrix[i] + matrix[j] + matrix[k] == 0:
                print(str(matrix[i]) + " " + str(matrix[j]) + " " + str(matrix[k]))
            else:
                print("Not any Triplet")