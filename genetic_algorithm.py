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

    def print(self, gen):
        print("Gen: {0} Min cost: {1} in gen: {2} sequence: {3}"
              .format(gen, self.minimal_sum, self.generation, self.minimal_comb))


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


def tournament_selection(population, prices, generation):
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
            min_conf.change_min(rhs_sum, seq_pop[rhs_index], generation)
        elif lhs_sum < rhs_sum:
            new_population.append(population[lhs_index])
            min_conf.change_min(lhs_sum, seq_pop[lhs_index], generation)

    if generation % 10 == 0 or generation == 1:
        min_conf.print(generation)

    if len(population) % 2 != 0:
        new_population.append(population[seq[-1]])
    return new_population


def display_results(gen):
    min_conf.print(gen)


def stop_dynamic_condition(gen, dynamic):
    global min_conf
    ret_value = False
    if gen >= min_conf.generation + dynamic:
        ret_value = True
    return ret_value


def reset():
    min_conf.reset()


def mutate_population(pop, percentage):
    num_of_mutations = calc_mutations_num(pop, percentage)

    mutations_index = np.arange(0, len(pop))
    np.random.shuffle(mutations_index)

    for i in range(num_of_mutations):
        mutate(pop[mutations_index[i]])
    return pop


def calc_mutations_num(population, percent):
    num_of_mutations = int(len(population) * percent / 100)
    if not num_of_mutations:
        num_of_mutations = 1
    return num_of_mutations


def mutate(one_object):
    index = randint(0, len(one_object) - 1)
    one_object[index] = randint(0, 255)

