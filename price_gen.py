import numpy as np

NUM_OF_CITIES = 4
MIN_PRICE = 10
MAX_PRICE = 50

FILE_NAME = "price_matrix.txt"


def set_configuration(num_of_cities, min_price, max_price):
    global NUM_OF_CITIES, MIN_PRICE, MAX_PRICE
    NUM_OF_CITIES = num_of_cities
    MIN_PRICE = min_price
    MAX_PRICE = max_price


def generate_prices():
    delta = MAX_PRICE - MIN_PRICE
    matrix = MIN_PRICE + delta * np.random.rand(NUM_OF_CITIES, NUM_OF_CITIES)
    np.fill_diagonal(matrix, 0)
    matrix = matrix.astype(np.int8)

    np.savetxt(FILE_NAME, matrix)

    return matrix


def load_from_file():
    matrix = np.loadtxt(FILE_NAME)
    matrix = matrix.astype(np.int8)
    return matrix
