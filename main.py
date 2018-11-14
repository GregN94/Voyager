import price_gen
import population as pop
import numpy as np

file_exist = False

if not file_exist:
    price_gen.set_configuration(3, 10, 50)
    pop.set_configuration(3, 10)
    price_gen.generate_prices_file()

price_matrix = price_gen.load_from_file()
# print(price_matrix)

population = pop.create_population()
# print(population)

# print(price_gen.generate_prices())

# print(price_matrix)


def symetric_matrix():
    [x, y] = np.triu_indices(4, k=1)
    m = np.zeros([4, 4])
    m = m.astype(int)

    rand_matrix = 10 + 40 * np.random.rand(6)
    m[x, y] = rand_matrix
    m[y, x] = rand_matrix
    return m

print(price_gen.symmetric_matrix(4))
