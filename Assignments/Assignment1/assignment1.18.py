def get_matrix_dimensions():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    return rows, cols


def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = float(input(f"Enter the value for element ({i+1},{j+1}): "))
            row.append(value)
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)


def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Cannot add matrices. Invalid dimensions.")
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            value = matrix1[i][j] + matrix2[i][j]
            row.append(value)
        result.append(row)
    return result


def subtract_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Cannot subtract matrices. Invalid dimensions.")
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            value = matrix1[i][j] - matrix2[i][j]
            row.append(value)
        result.append(row)
    return result


def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Cannot multiply matrices. Invalid dimensions.")
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


# Get dimensions of matrices from the user
rows1, cols1 = get_matrix_dimensions()
rows2, cols2 = get_matrix_dimensions()

# Create matrices
print("Enter values for matrix 1:")
matrix1 = create_matrix(rows1, cols1)

print("Enter values for matrix 2:")
matrix2 = create_matrix(rows2, cols2)

# Addition
try:
    addition_result = add_matrices(matrix1, matrix2)
    print("Addition result:")
    print_matrix(addition_result)
except ValueError as e:
    print(e)

# Subtraction
try:
    subtraction_result = subtract_matrices(matrix1, matrix2)
    print("Subtraction result:")
    print_matrix(subtraction_result)
except ValueError as e:
    print(e)

# Multiplication
try:
    multiplication_result = multiply_matrices(matrix1, matrix2)
    print("Multiplication result:")
    print_matrix(multiplication_result)
except ValueError as e:
    print(e)
