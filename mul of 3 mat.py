A = [
    [1, 1, 1],
    [2, 2, 2], 
    [3, 3, 3]
]
B = [
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
]
C = [
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
]
temp = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(3):
    for j in range(3):
        for k in range(3):
            temp[i][j] += A[i][k] * B[k][j]
result = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(3):
    for j in range(3):
        for k in range(3):
            result[i][j] += temp[i][k] * C[k][j]
print("First matrix elements:")
for row in A:
    print(*row)
print("\nSecond matrix elements:")  
for row in B:
    print(*row)
print("\nThird matrix elements:")
for row in C:
    print(*row)
print("\nMultiplication of the matrix:")
for row in result:
    print(*row)
