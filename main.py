import price_gen
import population as pop
import exact_solution
from timeit import default_timer as timer

import tkinter as tk

create_new_prices = True
find_exact_solution = True

NUM_OF_CITIES = 5
MIN_PRICE = 10
MAX_PRICE = 50

POPULATION_SIZE = 4


price_matrix = []


def calculate_exact_solution(matrix):
    start = timer()
    [value, comb] = exact_solution.calculate(matrix)
    print("The cheapest route is: {0}\nwith cost of {1} $".format(comb, value))
    end = timer()

    print("Spend time: {0} s".format(end - start))


def set_configuration():
    global num_of_cities, min_price, max_price
    price_gen.set_configuration(int(num_of_cities.get()), int(min_price.get()), int(max_price.get()))
    pop.set_configuration(int(num_of_cities.get()), POPULATION_SIZE)


def main():
    if create_new_prices:
        generate_new_prices()

    load_old_prices()

    population = pop.create_population()

    print("Price matrix:\n {0}".format(price_matrix))

    if find_exact_solution:
        calculate_exact_solution(price_matrix)


def load_old_prices():
    global  price_matrix
    price_matrix = price_gen.load_from_file()


def generate_new_prices():
    global price_matrix
    set_configuration()
    price_gen.generate_prices_file()
    price_matrix = price_gen.load_from_file()


def select_old():
    global check_new, create_new_prices, num_of_cities, min_price, max_price
    create_new_prices = False
    check_new.deselect()
    num_of_cities.config(state="disabled")
    min_price.config(state="disabled")
    max_price.config(state="disabled")


def select_new():
    global check_old, create_new_prices, num_of_cities, min_price, max_price
    create_new_prices = True
    check_old.deselect()
    num_of_cities.config(state="normal")
    min_price.config(state="normal")
    max_price.config(state="normal")


def create_checkbox(master):
    checkbox_frame = tk.Frame(master)
    checkbox_frame.pack()

    old = tk.Checkbutton(checkbox_frame, text="Load previous prices saved in file", command=select_old)
    old.pack(side=tk.LEFT)

    new = tk.Checkbutton(checkbox_frame, text="Generate new prices", command=select_new)
    new.pack(side=tk.RIGHT)
    return old, new


def create_price_conf_panel(master):
    price_conf_panel = tk.Frame(master)
    price_conf_panel.pack(side=tk.RIGHT)

    first_row = tk.Frame(price_conf_panel)
    first_row.pack()
    second_row = tk.Frame(price_conf_panel)
    second_row.pack()
    third_row = tk.Frame(price_conf_panel)
    third_row.pack()

    tk.Label(first_row, text="Num of cities").pack(side=tk.LEFT)
    tk.Label(second_row, text="Min price").pack(side=tk.LEFT)
    tk.Label(third_row, text="Max price").pack(side=tk.LEFT)

    number_of_cities = tk.Entry(first_row)
    minimum_price = tk.Entry(second_row)
    maximum_price = tk.Entry(third_row)

    number_of_cities.pack(side=tk.RIGHT)
    minimum_price.pack(side=tk.RIGHT)
    maximum_price.pack(side=tk.RIGHT)
    return number_of_cities, minimum_price, maximum_price


root = tk.Tk()
root.title("Comi Voyager")

root.wm_minsize(600, 100)
w = tk.Label(root, text="Prices configuration:")
w.pack()

check_old, check_new = create_checkbox(root)

num_of_cities, min_price, max_price = create_price_conf_panel(root)


check_old.select()
select_old()


frame = tk.Frame(root)
frame.pack(side=tk.BOTTOM)


down = tk.Button(text="Generate", command=main)
down.pack(side=tk.BOTTOM)

root.mainloop()


