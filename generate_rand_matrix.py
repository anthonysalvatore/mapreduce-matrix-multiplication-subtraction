import numpy as np


def generate_matrix(matrix_id=0, size=(2, 2), max_val=9):
    row, col = size[0], size[1]
    matrix = np.random.randint(1,max_val, size=(row, col))
    matrix_formatted = ''
    for r in range(row):
        matrix_formatted += f"{matrix_id}, {r}"
        for c in range(col):
            matrix_formatted += f', {matrix[r][c]}'
        matrix_formatted += '\n'
    print(matrix)
    return matrix_formatted

m = generate_matrix(3, (6, 6), 150)
with open('gen_matrixX.txt', 'w') as f:
    f.write(m)

