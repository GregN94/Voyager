import numpy as np


def create_cross_points(max_value, num_of_points):
    posiible_positions = np.arange(1, max_value)
    np.random.shuffle(posiible_positions)
    cross_position = sorted(posiible_positions[:num_of_points])
    return cross_position


def one_point_cross(first, second):
    cross_pos = create_cross_points(len(first), 1)

    new_1 = first[0: cross_pos[0]] + second[cross_pos[0]:]

    new_2 = second[0: cross_pos[0]] + first[cross_pos[0]:]
    return new_1, new_2


def two_point_cross(first, second):
    cross_pos = create_cross_points(len(first), 2)

    new_1 = first[0: cross_pos[0]] + second[cross_pos[0]: cross_pos[1]] + first[cross_pos[1]:]

    new_2 = second[0: cross_pos[0]] + first[cross_pos[0]: cross_pos[1]] + second[cross_pos[1]:]
    return new_1, new_2


def three_point_cross(first, second):
    cross_pos = create_cross_points(len(first), 3)

    new_1 = first[0: cross_pos[0]] + second[cross_pos[0]: cross_pos[1]] + first[cross_pos[1]: cross_pos[2]] + second[cross_pos[2]:]
    new_2 = second[0: cross_pos[0]] + first[cross_pos[0]: cross_pos[1]] + second[cross_pos[1]: cross_pos[2]] + first[cross_pos[2]:]
    return new_1, new_2


def four_point_cross(first, second):
    cross_pos = create_cross_points(len(first), 4)

    new_1 = first[0: cross_pos[0]] + second[cross_pos[0]: cross_pos[1]] + first[cross_pos[1]: cross_pos[2]] + second[cross_pos[2]:cross_pos[3]] + first[cross_pos[3]:]

    new_2 = second[0: cross_pos[0]] + first[cross_pos[0]: cross_pos[1]] + second[cross_pos[1]: cross_pos[2]] + first[cross_pos[2]:cross_pos[3]] + second[cross_pos[3]:]
    return new_1, new_2


def cross_spieces(first, second, cross_section):
    switch = {
        1: one_point_cross,
        2: two_point_cross,
        3: three_point_cross,
        4: four_point_cross
    }
    return switch[cross_section](first, second)
