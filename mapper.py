#!/usr/bin/env python3
# mapper for X-MN matrix function
# matrix input should be in form of 'matrix_identifier,row_number,[row values]', 1 is matrix M, 2 is matrix N, 3 is matrix X
# parameter input should be rows of matrix M, and columns in matrix N

import sys

m = int(sys.argv[1])  # rows in M
n = int(sys.argv[2])  # cols in N

# input comes from stdin
for line in sys.stdin:

    line = line.strip()
    field = line.split(",")
    field = [f.strip() for f in field]  # if spaces between entries

    matrix_num, row = int(field[0]), int(field[1])  # which matrix; row val is index 1

    for col, value in enumerate(field[2:]):
        # matrix M
        if matrix_num == 1:
            # generate number of key value pairs
            for k in range(n):
                print(f'{row},{k}\tM,{col},{value}')

        # matrix N
        elif matrix_num == 2:
            # generate number of key value pairs
            for k in range(m):
                print(f'{k},{col}\tN,{row},{value}')

        # matrix X
        else:
            print(f'{row},{col}\tX,{-1},{value}')
