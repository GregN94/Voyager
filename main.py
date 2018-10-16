import price_gen

price_gen.set_configuration(3, 25, 30)
matrix = price_gen.generate_prices()

print(matrix)
print(price_gen.load_from_file())


