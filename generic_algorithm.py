import numpy as np
from exact_solution import calculate_sum
from population import create_sequences_matrix
from random import *

INIT_MINIMAL_VALUE = 100000000000


class MinConfiguration:
    def __init__(self):
        self.minimal_sum = INIT_MINIMAL_VALUE
        self.minimal_comb = []
        self.generation = 0

    def change_min(self, p_sum, comb, gen):
        if p_sum < self.minimal_sum:
            self.minimal_sum = p_sum
            self.minimal_comb = comb
            self.generation = gen

    def reset(self):
        self.minimal_sum = INIT_MINIMAL_VALUE
        self.minimal_comb = []
        self.generation = 0

    def print(self):
        print("Min sum:" + str(self.minimal_sum) + " comb: " + str(self.minimal_comb))


min_conf = MinConfiguration()


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
    global min_conf
    new_population = []
    seq = np.arange(0, len(population))
    np.random.shuffle(seq)
    length = int(len(seq) / 2)
    seq_pop = create_sequences_matrix(population)
    for i in range(length):
        lhs_index = seq[2 * i]
        rhs_index = seq[2 * i + 1]
        lhs_sum = calculate_sum(seq_pop[lhs_index], prices)
        rhs_sum = calculate_sum(seq_pop[rhs_index], prices)
        if lhs_sum >= rhs_sum:
            new_population.append(population[rhs_index])
            min_conf.change_min(rhs_sum, population[rhs_index], 0)
        elif lhs_sum < rhs_sum:
            new_population.append(population[lhs_index])
            min_conf.change_min(lhs_sum, population[lhs_index], 0)

    min_conf.print()
    if len(population) % 2 is not 0:
        new_population.append(population[seq[len(seq) - 1]])
    return new_population


def reset():
    min_conf.reset()


def mutate_all_population(population, percent):
    # print(percent)
    num_of_mutations = int(len(population) * percent / 100)
    if num_of_mutations == 0:
        num_of_mutations = 1
    rand_pop_index = np.arange(0, len(population))
    np.random.shuffle(rand_pop_index)
    # print(population)
    for i in range(num_of_mutations):
        # print(rand_pop_index[i])
        mutate(population[rand_pop_index[i]])
    # cross_position = sorted(possible_positions[:num_of_points])
    # return cross_position
    # print(population)


def mutate(speciman):
    index = randint(0, len(speciman) - 1)
    # print(index)
    speciman[index] = randint(0, len(speciman) - 1)

