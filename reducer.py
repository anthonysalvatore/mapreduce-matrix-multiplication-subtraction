#!/usr/bin/env python
# reducer for X-NM matrix function

import sys

# initialise variables
current_key = None
current_value = 0
x_val = 0
values = dict()

for line in sys.stdin:

    line = line.strip()
    key, value = line.split('\t')  # read in every line, split on tab

    row, col = map(int, key.split(','))
    value = value.split(',')
    key = (row, col)  # key = row&col of final matrix
    matrix, pos, element_value = value[0], int(value[1]), int(value[2])  # retrieve info from mapper

    if key == current_key:

        if matrix == 'X':
            x_val = element_value  # store value from X matrix if line is from X matrix
        else:
            if pos not in values:
                values[pos] = [element_value]  # if pos not in dict, add
            else:
                values[pos].append(element_value)  # if pos in dict, append to key so both values can be multiplied later

    else:

        if current_key:  # if not first

            # loop through dict, multiplying values at same pos and adding to total value for current key
            for i in range(len(values)):
                current_value += values[i][0] * values[i][1]
            current_value = x_val - current_value
            print(f'{previous_row}\t{previous_col}\t{current_value}')  # emit row, col and value of final matrix as required

        # reset values to calculate new key
        current_key = key
        values = dict()
        x_val = 0
        current_value = 0

        # compute for first/new key
        if matrix == 'X':
            x_val = element_value
        else:
            values[pos] = [element_value]

        # store values for use in emitting
        previous_row, previous_col = row, col

# last entry
if current_key:
    for i in range(len(values)):
        current_value += values[i][0] * values[i][1]
    current_value = x_val - current_value
    print(f'{previous_row}\t{previous_col}\t{current_value}')
