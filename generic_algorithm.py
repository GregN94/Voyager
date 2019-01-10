import numpy as np
from exact_solution import calculate_sum


def create_cross_points(max_value, num_of_points):
    possible_positions = np.arange(1, max_value)
    np.random.shuffle(possible_positions)
    cross_position = sorted(possible_positions[:num_of_points])
    return cross_position


def execute(first, second, func):
    new_1 = func(first, second)
    new_2 = func(second, first)
    return new_1, new_2


def one_point_cross(first, second):
    pos = create_cross_points(len(first), 1)
    cross = lambda x, y: x[0: pos[0]] + y[pos[0]:]
    return execute(first, second, cross)


def two_point_cross(first, second):
    pos = create_cross_points(len(first), 2)
    cross = lambda x, y: x[0: pos[0]] + y[pos[0]: pos[1]] + x[pos[1]:]
    return execute(first, second, cross)


def three_point_cross(first, second):
    pos = create_cross_points(len(first), 3)
    cross = lambda x, y: x[0: pos[0]] + y[pos[0]: pos[1]] + x[pos[1]: pos[2]] + y[pos[2]:]
    return execute(first, second, cross)


def four_point_cross(first, second):
    pos = create_cross_points(len(first), 4)
    cross = lambda x, y: x[0: pos[0]] + y[pos[0]: pos[1]] + x[pos[1]: pos[2]] + y[pos[2]:pos[3]] + x[pos[3]:]
    return execute(first, second, cross)


def cross_two_specimens(first, second, cross_type):
    switch = {
        1: one_point_cross,
        2: two_point_cross,
        3: three_point_cross,
        4: four_point_cross
    }
    return switch[cross_type](first, second)


def cross_specimens(population, cross_type):
    population = population.tolist()
    possible_pos = np.arange(0, len(population))
    np.random.shuffle(possible_pos)
    length = int(len(possible_pos) / 2)
    new_population = []
    for i in range(length):
        [new_1, new_2] = cross_two_specimens(population[possible_pos[2 * i]],
                                             population[possible_pos[2 * i + 1]], cross_type)
        new_population.append(new_1)
        new_population.append(new_2)

    population.extend(new_population)
    return population


def tournament_selection(population, prices):
    print(population)
    seq = np.arange(0, len(population))
    np.random.shuffle(seq)
    length = int(len(seq) / 2)
    for i in range(length):
        print("Pair: {0} {1}".format(population[seq[2 * i]], population[seq[2 * i + 1]]))
        lhs = calculate_sum(population[seq[2 * i]], prices)
        rhs = calculate_sum(population[seq[2 * i + 1]], prices)
        print(lhs)
        print(rhs)
        
