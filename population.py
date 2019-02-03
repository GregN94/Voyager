import numpy as np
from collections import defaultdict

NUM_OF_CITIES = 4
POPULATION_SIZE = 4


def set_configuration(num_of_cities, population_size):
    global NUM_OF_CITIES, POPULATION_SIZE
    NUM_OF_CITIES = num_of_cities
    POPULATION_SIZE = population_size


def create_population():
    population = 255 * np.random.rand(POPULATION_SIZE, NUM_OF_CITIES)
    population = population.astype(np.uint8)
    return population


def create_sequences_matrix(population):
    sorted_matrix = []
    for specimen in population:
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
