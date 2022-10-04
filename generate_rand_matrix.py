import random


def generate_matrix(matrix_id=0, size=(2, 2), max_val=9):
    row, col = size[0], size[1]
    matrix_formatted = ''
    for r in range(row):
        matrix_formatted += f"{matrix_id}, {r}"
        for c in range(col):
            matrix_formatted += f', {random.randint(1,max_val)}'
        matrix_formatted += '\n'
    return matrix_formatted

m = generate_matrix(3, (200, 200), 300000)
with open('gen_matrixX.txt', 'w') as f:
    f.write(m)


