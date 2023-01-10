matrix = []
for i in range(3):
    a = list(map(int, input().split()))
    matrix.append(a)

res_matrix = matrix

for i in range(0, 3):
    for j in range(0, 3):

        if i == 0 and j == 0:
            print(1)
            if matrix[i][j] % 2 == 0:
                print(1)
                res_matrix[i][j] = (matrix[i][j] % 2)
                print(res_matrix[i][j])
                res_matrix[i][j+1] = matrix[i][j+1]
                res_matrix[i+1][j] = matrix[i+1][j]
            else:
                print(1)
                res_matrix[i][j] = ((matrix[i][j] + 1) % 2)
                print(res_matrix[i][j])
                res_matrix[i][j+1] = matrix[i][j+1] +1
                res_matrix[i+1][j] = matrix[i+1][j] +1
        if i == 0 and j == 1:
            if matrix[i][j] % 2 == 0:
                res_matrix[i][j] = (matrix[i][j] % 2)
                res_matrix[i][j+1] = matrix[i][j+1]
                res_matrix[i+1][j] = matrix[i+1][j]
                res_matrix[i][j-1] = matrix[i][j-1]
            else:
                res_matrix[i][j] = (matrix[i][j] % 2)
                res_matrix[i][j+1] = (matrix[i][j+1] +1) % 2
                res_matrix[i+1][j] = (matrix[i+1][j] +1)%2
                res_matrix[i][j-1] = (matrix[i][j-1] +1) % 2
        if i == 0 and j == 2:
            if matrix[i][j] % 2 == 0:
                res_matrix[i][j] = (matrix[i][j] % 2)
                res_matrix[i+1][j] = matrix[i+1][j]
                res_matrix[i][j-1] = matrix[i][j-1]
            else:
                res_matrix[i][j] = (matrix[i][j] % 2)
                res_matrix[i+1][j] = (matrix[i+1][j] +1)%2
                res_matrix[i][j-1] = (matrix[i][j-1] +1)%2
        if i == 1 and j == 0:
            if matrix[i][j] % 2 == 0:
                res_matrix[i][j] = (matrix[i][j] % 2)
                res_matrix[i][j+1] = matrix[i][j+1]
                res_matrix[i+1][j] = matrix[i+1][j]
                res_matrix[i-1][j] = matrix[i-1][j]
            else:
                res_matrix[i][j] = (matrix[i][j] % 2)
                res_matrix[i][j+1] = (matrix[i][j+1] +1)%2
                res_matrix[i+1][j] = (matrix[i+1][j] +1)%2
                res_matrix[i-1][j] = (matrix[i-1][j] +1)%2
        if i == 1 and j == 1:
            if matrix[i][j] % 2 == 0:
                res_matrix[i][j] = (matrix[i][j] % 2)
                res_matrix[i][j+1] = matrix[i][j+1]
                res_matrix[i+1][j] = matrix[i+1][j]
                res_matrix[i][j-1] = matrix[i][j-1]
                res_matrix[i-1][j] = matrix[i-1][j]

            else:
                res_matrix[i][j] = (matrix[i][j] % 2)
                res_matrix[i][j+1] = matrix[i][j+1] +1
                res_matrix[i+1][j] = (matrix[i+1][j] +1)%2
                res_matrix[i][j-1] = (matrix[i][j-1] +1)%2
                res_matrix[i-1][j] = (matrix[i-1][j] +1)%2
        if i == 1 and j == 2:
            if matrix[i][j] % 2 == 0:
                res_matrix[i][j] = (matrix[i][j] % 2)
                res_matrix[i+1][j] = matrix[i+1][j]
                res_matrix[i][j-1] = matrix[i][j-1]
                res_matrix[i-1][j] = matrix[i-1][j]

            else:
                res_matrix[i][j] = (matrix[i][j] % 2)
                res_matrix[i+1][j] = (matrix[i+1][j] +1)%2
                res_matrix[i][j-1] = (matrix[i][j-1] +1)%2
                res_matrix[i-1][j] = (matrix[i-1][j] +1)%2
        if i == 2 and j == 0:
            if matrix[i][j] % 2 == 0:
                res_matrix[i][j] = (matrix[i][j] % 2)
                res_matrix[i][j+1] = matrix[i][j+1]
                res_matrix[i-1][j] = matrix[i-1][j]

            else:
                res_matrix[i][j] = (matrix[i][j] % 2)
                res_matrix[i][j+1] = (matrix[i][j+1] +1)%2
                res_matrix[i-1][j] = (matrix[i-1][j] +1)%2

        if i == 2 and j == 1:
            if matrix[i][j] % 2 == 0:
                res_matrix[i][j] = (matrix[i][j] % 2)
                res_matrix[i][j+1] = matrix[i][j+1]
                res_matrix[i][j-1] = matrix[i][j-1]
                res_matrix[i-1][j] = matrix[i-1][j]

            else:
                res_matrix[i][j] = (matrix[i][j] % 2)
                res_matrix[i][j+1] = (matrix[i][j+1] +1)%2
                res_matrix[i][j-1] = (matrix[i][j-1] +1)%2
                res_matrix[i-1][j] = (matrix[i-1][j] +1)%2
        if i == 2 and j == 2:
            if matrix[i][j] % 2 == 0:
                res_matrix[i][j] = (matrix[i][j] % 2)
                res_matrix[i][j-1] = matrix[i][j-1]
                res_matrix[i-1][j] = matrix[i-1][j]

            else:
                res_matrix[i][j] = (matrix[i][j] % 2)
                res_matrix[i][j-1] = (matrix[i][j-1] +1)%2
                res_matrix[i-1][j] = (matrix[i-1][j] +1)%2


print(res_matrix)
                


