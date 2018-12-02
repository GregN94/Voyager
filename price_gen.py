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


def generate_prices(size):
    [x, y] = np.triu_indices(size, k=1)
    matrix = np.zeros([size, size]).astype(int)
    delta = MAX_PRICE - MIN_PRICE
    num_of_elements = ((size - 1) * size) / 2
    rand_matrix = MIN_PRICE + delta * np.random.rand(int(num_of_elements))
    matrix[x, y] = rand_matrix
    matrix[y, x] = rand_matrix
    return matrix


def generate_prices_file():
    matrix = generate_prices(NUM_OF_CITIES)
    np.savetxt(FILE_NAME, matrix)


def load_from_file():
    matrix = np.loadtxt(FILE_NAME)
    matrix = matrix.astype(np.int8)
    return matrix


