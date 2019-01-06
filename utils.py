from tkinter import messagebox
from enum import Enum


class Stop(Enum):
    DYNAMIC = 0
    STATIC = 1


def check_entry(entry, value, string):
    entry.configure(background="white")
    if not entry.get() or int(entry.get()) <= value:
        entry.configure(background="#FF9999")
        messagebox.showerror("Incorrect value", "{0} should be bigger than {1}".format(string, value))
        return False
    return True


def check_checkbox(checkbox, values, string):
    checkbox.configure(background="white")
    is_correct = False
    if checkbox.get():
        for value in values:
            if int(checkbox.get()) is value:
                is_correct = True
    if not is_correct:
        checkbox.configure(background="#FF9999")
        messagebox.showerror("Incorrect value", "{0} should be picked from {1}".format(string, values))
    return is_correct


def int_from_entry(entry, default_value):
    if entry.get():
        default_value = int(entry.get())
    return default_value


def AND(*args):
    logic = True
    for arg in args:
        logic = logic and arg
    return logic

