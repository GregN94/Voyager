import numpy as np
import itertools


# functions definitions
def calculate_sum(comb, matrix, matrix_size):
    sum = 0
    for i in range(matrix_size):
        if i == 0:
            continue
        sum += matrix[comb[i - 1], comb[i]]
    return sum


def calculate(matrix):
    size = matrix.shape[0]
    min_val = 1000
    min_comb = 0
    combinations = itertools.permutations(range(size), size)
    for comb in combinations:
        ret = calculate_sum(comb, matrix, size)
        if ret < min_val:
            min_val = ret
            min_comb = comb
    return min_val, min_comb
