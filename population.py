import numpy as np

NUM_OF_CITIES = 4
POPULATION_SIZE = 4


def set_configuration(num_of_cities, population_size):
    global NUM_OF_CITIES, POPULATION_SIZE
    NUM_OF_CITIES = num_of_cities
    POPULATION_SIZE = population_size


def create_population():
    population = NUM_OF_CITIES * np.random.rand(POPULATION_SIZE, NUM_OF_CITIES)
    population = population.astype(np.int8)
    return population

