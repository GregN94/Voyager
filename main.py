import price_gen
import population as pop
import exact_solution
from timeit import default_timer as timer


NUM_OF_CITIES = 5
MIN_PRICE = 10
MAX_PRICE = 50

POPULATION_SIZE = 4


class Engine:
    def __init__(self):
        self.price_matrix = []
        self.num_of_cities = NUM_OF_CITIES
        self.min_price = MIN_PRICE
        self.max_price = MAX_PRICE

    def set_configuration(self):
        price_gen.set_configuration(self.num_of_cities, self.min_price, self.max_price)
        pop.set_configuration(self.num_of_cities, POPULATION_SIZE)

    def run_exact_solution(self):
        print("Price matrix:\n {0}".format(self.price_matrix))
        start = timer()
        [value, comb] = exact_solution.calculate(self.price_matrix)
        print("The cheapest route is: {0}\nwith cost of {1} $".format(comb, value))
        end = timer()
        print("Spend time: {0} s".format(end - start))

    def load_prices(self):
        if price_gen.check_if_price_file_exist():
            self.price_matrix = price_gen.load_from_file()
            file_exist = True
        else:
            self.price_matrix = price_gen.generate_prices_file()
            file_exist = False
        return file_exist

    def generate_new_prices(self):
        self.set_configuration()
        price_gen.generate_prices_file()
        self.price_matrix = price_gen.load_from_file()


