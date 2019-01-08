import price_gen
import population as pop
import exact_solution
from timeit import default_timer as timer
from tkinter import messagebox
from utils import Stop
import generic_algorithm


NUM_OF_CITIES = 5
MIN_PRICE = 10
MAX_PRICE = 50

POPULATION_SIZE = 4
MUTATION_PERCENTAGE = 5
MIXING_TYPE = 2

GENERATIONS_RANGE = 1000
GENERATIONS_TO_END = 10000


class Engine:
    def __init__(self):
        self.price_matrix = []
        self.num_of_cities = NUM_OF_CITIES
        self.min_price = MIN_PRICE
        self.max_price = MAX_PRICE

        self.population_size = POPULATION_SIZE
        self.mutation_percentage = MUTATION_PERCENTAGE
        self.mixing_type = MIXING_TYPE

        self.stop_condition = Stop.DYNAMIC
        self.generations_range = GENERATIONS_RANGE
        self.generations_to_end = GENERATIONS_TO_END

    def set_configuration(self):
        price_gen.set_configuration(self.num_of_cities, self.min_price, self.max_price)
        pop.set_configuration(self.num_of_cities, POPULATION_SIZE)

    def exact_solution(self):
        if not self.load_prices_file():
            self.default_prices()

        messagebox.showinfo("Simple solution",
                            "Running exact solution, it might take a while")
        self.print_price_matrix()
        start = timer()
        [value, comb] = exact_solution.calculate(self.price_matrix)
        print("The cheapest route is: {0}\nwith cost of {1} $".format(comb, value))
        end = timer()
        print("Spend time: {0} s".format(end - start))

    def print_price_matrix(self):
        print("Price matrix:\n {0}".format(self.price_matrix))

    def default_prices(self):
        messagebox.showinfo("Default configuration",
                            "There was no previous configuration, running with default configuration")
        self.price_matrix = price_gen.generate_prices_file()

    def load_prices_file(self):
        does_file_exist = False

        if price_gen.check_if_price_file_exist():
            self.price_matrix = price_gen.load_from_file()
            self.num_of_cities = len(self.price_matrix)
            does_file_exist = True

        return does_file_exist

    def generate_new_prices(self):
        self.set_configuration()
        price_gen.generate_prices_file()

    def set_algorithm_settings(self, population, mixing, mutation, stop, gen_range=GENERATIONS_RANGE, gen_end=GENERATIONS_TO_END):
        self.population_size = population
        self.mixing_type = mixing
        self.mutation_percentage = mutation
        self.stop_condition = stop

        if self.stop_condition is Stop.DYNAMIC:
            self.generations_range = gen_range
        else:
            self.generations_to_end = gen_end

    def generic_algorithm(self):
        if not self.load_prices_file():
            self.default_prices()
        self.print_price_matrix()
        pop.set_configuration(self.num_of_cities, self.population_size)
        population = pop.create_population()
        print(population)
        # for i in population:
        #     print(exact_solution.calculate_sum(i, self.price_matrix))

        generic_algorithm.cross_specimens(population)
