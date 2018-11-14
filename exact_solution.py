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


def find_min(matrix, matrix_size):
    min_val = 1000
    combinations = itertools.permutations(range(matrix_size), matrix_size)
    for comb in combinations:
        ret = calculate_sum(comb, matrix, matrix_size)
        if ret < min_val:
            min_val = ret
    return min_val


# 3x3 matrix test
price_matrix_test_3x3 = np.matrix([[0, 10, 15],
                                   [10, 0, 20],
                                   [15, 20, 0]])

print(find_min(price_matrix_test_3x3, 3))


# 4x4 matrix test
price_matrix_test_4x4 = np.matrix([[0, 10, 15, 20],
                                   [10, 0, 20, 30],
                                   [15, 20, 0, 10],
                                   [20, 30, 10, 0]])

print(find_min(price_matrix_test_4x4, 4))
