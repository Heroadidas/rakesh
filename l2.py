import numpy as np
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)

# Matrix Addition
print("\nMatrix Addition (A + B):")
print(A + B)
# Matrix Subtraction
print("\nMatrix Subtraction (A - B):")
print(A - B)
# Element-wise Matrix Multiplication
print("\nElement-wise Matrix Multiplication (A * B):")
print(A * B)
# Transpose of Matrix A
print("\nTranspose of Matrix A:")
print(A.T)
# Matrix Multiplication (A * B^T)
F = np.dot(A, B.T)
print("\nMatrix Multiplication (A * B^T):")
print(F)

batch_size = 16
input_features = 10
output_features = 5
input_batch = np.random.randint(0, 101, size=(batch_size, input_features))
weights = np.random.randint(0, 101, size=(input_features, output_features))
output_batch = np.dot(input_batch, weights)
print("Input Batch (16 samples, each with 10 features ranging from 0 to 100):")
print(input_batch)
print("\nWeight Matrix (10 input features, 5 output features ranging from 0 to 100):")
print(weights)
print("\nOutput Batch Shape (16 samples, each with 5 output features):")
print(output_batch)

A = np.random.randint(1, 101, size=(3, 4))
B = np.random.randint(1, 101, size=(3, 4))
print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
concatenated_matrix = np.concatenate((A, B), axis=1)
print("\nConcatenated Matrix (A concatenated with B along columns):")
print(concatenated_matrix)
part1, part2 = np.split(concatenated_matrix, 2, axis=1)
print("\nPart 1 after Splitting:")
print(part1)
print("\nPart 2 after Splitting:")
print(part2)
print("\nShapes:")
print("Matrix A Shape:", A.shape)
print("Matrix B Shape:", B.shape)
print("Concatenated Matrix Shape:", concatenated_matrix.shape)
print("Part 1 Shape after Splitting:", part1.shape)
print("Part 2 Shape after Splitting:", part2.shape)

A = np.array([[1, 2], [3, 4]])
print("Matrix A:")
print(A)
# Compute matrix rank
rank_A = np.linalg.matrix_rank(A)
print("\nMatrix Rank of A:", rank_A)
# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("\nEigenvalues of A:")
print(eigenvalues)
print("\nEigenvectors of A:")
print(eigenvectors)
# Compute matrix inverse
A_inv = np.linalg.inv(A)
print("\nInverse of Matrix A:")
print(A_inv)