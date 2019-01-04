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


class PriceConfigPanel:
    def __init__(self, top=None):
        font10 = "-family {DejaVu Sans} -size 13 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        self.price_conf_lbl = tk.Label(top)
        self.price_conf_lbl.place(relx=0.224, rely=0.029, height=20, width=262)
        self.price_conf_lbl.configure(activebackground="#f9f9f9")
        self.price_conf_lbl.configure(font=font10)
        self.price_conf_lbl.configure(text="Price matrix configuration")
        self.price_conf_lbl.configure(width=262)

        self.min_price_lbl = tk.Label(top)
        self.min_price_lbl.place(relx=0.551, rely=0.19, height=21, width=64)
        self.min_price_lbl.configure(activebackground="#f9f9f9")
        self.min_price_lbl.configure(text="Min price")

        self.max_price_lbl = tk.Label(top)
        self.max_price_lbl.place(relx=0.551, rely=0.234, height=21, width=68)
        self.max_price_lbl.configure(activebackground="#f9f9f9")
        self.max_price_lbl.configure(text="Max price")

        self.num_of_cities_lbl = tk.Label(top)
        self.num_of_cities_lbl.place(relx=0.551, rely=0.146, height=21, width=91)
        self.num_of_cities_lbl.configure(activebackground="#f9f9f9")
        self.num_of_cities_lbl.configure(text="Num of cities")

        self.old_matrix_checkbox = tk.Checkbutton(top)
        self.old_matrix_checkbox.place(relx=0.041, rely=0.088, relheight=0.034, relwidth=0.41)
        self.old_matrix_checkbox.configure(activebackground="#f9f9f9")
        self.old_matrix_checkbox.configure(justify='left')
        self.old_matrix_checkbox.configure(text="Load previous price matrix")
        self.old_matrix_checkbox.configure(command=self.select_old)

        self.new_matrix_checkbox = tk.Checkbutton(top)
        self.new_matrix_checkbox.place(relx=0.531, rely=0.088, relheight=0.034, relwidth=0.376)
        self.new_matrix_checkbox.configure(activebackground="#f9f9f9")
        self.new_matrix_checkbox.configure(justify='left')
        self.new_matrix_checkbox.configure(text="Create new price matrix")
        self.new_matrix_checkbox.configure(command=self.select_new)

        self.num_of_cities_entry = tk.Entry(top)
        self.num_of_cities_entry.place(relx=0.755, rely=0.146, height=23, relwidth=0.196)
        self.num_of_cities_entry.configure(background="white")
        self.num_of_cities_entry.configure(font="TkFixedFont")
        self.num_of_cities_entry.configure(selectbackground="#c4c4c4")

        self.min_price_entry = tk.Entry(top)
        self.min_price_entry.place(relx=0.755, rely=0.19, height=23, relwidth=0.196)
        self.min_price_entry.configure(background="white")
        self.min_price_entry.configure(font="TkFixedFont")
        self.min_price_entry.configure(selectbackground="#c4c4c4")

        self.max_price_entry = tk.Entry(top)
        self.max_price_entry.place(relx=0.755, rely=0.234, height=23, relwidth=0.196)
        self.max_price_entry.configure(background="white")
        self.max_price_entry.configure(font="TkFixedFont")
        self.max_price_entry.configure(selectbackground="#c4c4c4")

        self.create_new_prices = True

    def get_num_of_cities(self):
        return int(self.num_of_cities_entry.get())

    def get_min_price(self):
        return int(self.min_price_entry.get())

    def get_max_price(self):
        return int(self.max_price_entry.get())

    def select_old(self):
        self.create_new_prices = False
        self.new_matrix_checkbox.deselect()
        self.num_of_cities_entry.config(state="disabled")
        self.min_price_entry.config(state="disabled")
        self.max_price_entry.config(state="disabled")

    def select_new(self):
        self.create_new_prices = True
        self.old_matrix_checkbox.deselect()
        self.num_of_cities_entry.config(state="normal")
        self.min_price_entry.config(state="normal")
        self.max_price_entry.config(state="normal")

    def check_matrix_conf(self):
        return AND(check_entry(self.num_of_cities_entry, 2, "Number of cities"),
                   check_entry(self.min_price_entry, 1, "Min price"),
                   check_entry(self.max_price_entry, int_from_entry(self.min_price_entry, 2), "Max price"))

