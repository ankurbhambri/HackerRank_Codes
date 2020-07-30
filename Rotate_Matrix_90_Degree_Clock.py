# Function to print the matrix
def print_matrix(mat):
    for i in range (len(mat)):
        for j in range (len(mat)):
            print(str(mat[i][j]), end = " ")
        print()

# Function to transpose the matrix
def transpose_matrix(mat):
    for i in range(len(mat)): 
        for j in range(i, len(mat)):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

# Function to rotate the matrix clock wise
def clock_wise_rotate(mat):
    for i in range(len(mat)):
        k = len(mat) - 1
        aa = 1
        for j in range(k):
            if k >= 1:
                mat[i][j], mat[i][k] = mat[i][k], mat[i][j]
                k = k - aa
                aa += 1


# Main Function
mat = [[1,2,3],[4,5,6],[7,8,9]]
print("The array before rotation is ")
print_matrix(mat)

transpose_matrix(mat)
clock_wise_rotate(mat)

print("\nThe array after rotation is ")
print_matrix(mat)

# mat 2
mat2 = [[1, 2, 3, 4], [5, 6, 7, 8 ], [9, 10, 11, 12],[13, 14, 15, 16]]
print("The array before rotation is ")
print_matrix(mat2)

transpose_matrix(mat2)
clock_wise_rotate(mat2)

print("\nThe array after rotation is ")
print_matrix(mat2)