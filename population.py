import numpy as np
from collections import defaultdict
from exact_solution import calculate_sum

NUM_OF_CITIES = 4
POPULATION_SIZE = 4


def set_configuration(num_of_cities, population_size):
    global NUM_OF_CITIES, POPULATION_SIZE
    NUM_OF_CITIES = num_of_cities
    POPULATION_SIZE = population_size


def create_population_matrix():
    population = NUM_OF_CITIES * np.random.rand(POPULATION_SIZE, NUM_OF_CITIES)
    population = population.astype(np.uint8)
    return population


def create_population():
    matrix = create_population_matrix()
    sorted_matrix = []
    for specimen in matrix:
        index = 0
        data_dict = defaultdict(list)
        for value in specimen:
            data_dict[value].append(index)
            index += 1
        data_dict = sorted(data_dict.items())
        sorted_matrix.append(create_list_from_dict(data_dict))
    return sorted_matrix


def create_list_from_dict(data_dict):
    list_seq = []
    for elem in data_dict:
        for iter in range(len(elem[1])):
            list_seq.append(elem[1][iter])
    return list_seq
