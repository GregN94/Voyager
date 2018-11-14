import price_gen
import population as pop


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
