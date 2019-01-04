try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from tkinter import messagebox
from utils import *

MIXING_TYPES = [1, 2, 3, 4]
MUTATION_PERCENTAGE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


class AlgorithmConfigPanel:
    def __init__(self, top=None):
        font10 = "-family {DejaVu Sans} -size 13 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font9 = "-family {DejaVu Sans} -size 12 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.gen_alg_conf_lbl = tk.Label(top)
        self.gen_alg_conf_lbl.place(relx=0.163, rely=0.512, height=26, width=287)
        self.gen_alg_conf_lbl.configure(activebackground="#f9f9f9")
        self.gen_alg_conf_lbl.configure(font=font10)
        self.gen_alg_conf_lbl.configure(text="Generic Algorithm configuration")

        self.population_size_lbl = tk.Label(top)
        self.population_size_lbl.place(relx=0.041, rely=0.57, height=21, width=103)
        self.population_size_lbl.configure(activebackground="#f9f9f9")
        self.population_size_lbl.configure(text="Population size")

        self.mixing_type_lbl = tk.Label(top)
        self.mixing_type_lbl.place(relx=0.49, rely=0.57, height=21, width=100)
        self.mixing_type_lbl.configure(activebackground="#f9f9f9")
        self.mixing_type_lbl.configure(text="Mixing type")

        self.mutation_percentage_lbl = tk.Label(top)
        self.mutation_percentage_lbl.place(relx=0.041, rely=0.614, height=21, width=79)
        self.mutation_percentage_lbl.configure(activebackground="#f9f9f9")
        self.mutation_percentage_lbl.configure(text="Mutation %")

        self.stop_condition_lbl = tk.Label(top)
        self.stop_condition_lbl.place(relx=0.347, rely=0.702, height=23, width=118)
        self.stop_condition_lbl.configure(activebackground="#f9f9f9")
        self.stop_condition_lbl.configure(font=font9)
        self.stop_condition_lbl.configure(text="Stop condition")

        self.generations_to_end_lbl = tk.Label(top)
        self.generations_to_end_lbl.place(relx=0.082, rely=0.789, height=21, width=128)
        self.generations_to_end_lbl.configure(activebackground="#f9f9f9")
        self.generations_to_end_lbl.configure(text="Generations to end")

        self.generations_range_lbl = tk.Label(top)
        self.generations_range_lbl.place(relx=0.551, rely=0.789, height=21, width=124)
        self.generations_range_lbl.configure(activebackground="#f9f9f9")
        self.generations_range_lbl.configure(text="Generations range")

        self.population_size_entry = tk.Entry(top)
        self.population_size_entry.place(relx=0.286, rely=0.57, height=23, relwidth=0.135)
        self.population_size_entry.configure(background="white")
        self.population_size_entry.configure(font="TkFixedFont")
        self.population_size_entry.configure(selectbackground="#c4c4c4")

        self.mixing_type_box = ttk.Combobox(top, values=MIXING_TYPES)
        self.mixing_type_box.place(relx=0.694, rely=0.57, relheight=0.031, relwidth=0.137)
        self.mixing_type_box.configure(background="#000000")
        self.mixing_type_box.configure(takefocus="")

        self.mutation_percentage_box = ttk.Combobox(top, values=MUTATION_PERCENTAGE)
        self.mutation_percentage_box.place(relx=0.286, rely=0.614, relheight=0.031, relwidth=0.137)
        self.mutation_percentage_box.configure(takefocus="")

        self.static_stop_checkbox = tk.Checkbutton(top)
        self.static_stop_checkbox.place(relx=0.204, rely=0.746, relheight=0.034, relwidth=0.131)
        self.static_stop_checkbox.configure(activebackground="#f9f9f9")
        self.static_stop_checkbox.configure(justify='left')
        self.static_stop_checkbox.configure(text="Static")
        self.static_stop_checkbox.configure(command=self.select_static)

        self.dynamic_stop_checkbox = tk.Checkbutton(top)
        self.dynamic_stop_checkbox.place(relx=0.531, rely=0.746, relheight=0.034, relwidth=0.173)
        self.dynamic_stop_checkbox.configure(activebackground="#f9f9f9")
        self.dynamic_stop_checkbox.configure(justify='left')
        self.dynamic_stop_checkbox.configure(text="Dynamic")
        self.dynamic_stop_checkbox.configure(command=self.select_dynamic)

        self.generations_to_end_entry = tk.Entry(top)
        self.generations_to_end_entry.place(relx=0.082, rely=0.833, height=23, relwidth=0.176)
        self.generations_to_end_entry.configure(background="white")
        self.generations_to_end_entry.configure(font="TkFixedFont")
        self.generations_to_end_entry.configure(selectbackground="#c4c4c4")

        self.generations_range_entry = tk.Entry(top)
        self.generations_range_entry.place(relx=0.551, rely=0.833, height=23, relwidth=0.196)
        self.generations_range_entry.configure(background="white")
        self.generations_range_entry.configure(font="TkFixedFont")
        self.generations_range_entry.configure(selectbackground="#c4c4c4")

        self.stop_condition = Stop.DYNAMIC

    def get_population(self):
        return self.population_size_entry.get()

    def get_mutation(self):
        return self.mutation_percentage_box.get()

    def get_mixing(self):
        return self.mixing_type_box.get()

    def get_generation_range(self):
        return self.generations_range_entry.get()

    def get_generation_end(self):
        return self.generations_to_end_entry.get()

    def select_static(self):
        self.stop_condition = Stop.STATIC
        self.dynamic_stop_checkbox.deselect()
        self.generations_range_entry.config(state="disabled")
        self.generations_to_end_entry.config(state="normal")

    def select_dynamic(self):
        self.stop_condition = Stop.DYNAMIC
        self.static_stop_checkbox.deselect()
        self.generations_to_end_entry.config(state="disabled")
        self.generations_range_entry.config(state="normal")

    def check_algorithm_conf(self):
        return AND(check_entry(self.population_size_entry, 2, "Population"),
                   check_checkbox(self.mixing_type_box, MIXING_TYPES, "Mixing Types"),
                   check_checkbox(self.mutation_percentage_box, MUTATION_PERCENTAGE, "Mutation"),
                   self.check_stop_condition())

    def check_static_condition(self):
        return check_entry(self.generations_to_end_entry, 2, "Generations to end")

    def check_dynamic_condition(self):
        return check_entry(self.generations_range_entry, 2, "Generations range")

    def check_stop_condition(self):
        switch = {
            Stop.STATIC: self.check_static_condition,
            Stop.DYNAMIC: self.check_dynamic_condition
        }
        return switch.get(self.stop_condition, "Invalid")()

