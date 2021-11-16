# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 1
# Author: Nguyen Nguyen Khuong (s3924577)
# Created date: 16/11/2021
# Last modified date: 16/11/2021


def total_flour(large_thick, large_thin, medium_thick, medium_thin):
    return (large_thick * 550 + large_thin * 500 + medium_thick * 450 + medium_thin * 400) * 106 / 100000


def total_cost_A(flour):
    expense = flour * 30000
    if flour < 30:
        expense -= (expense * 3 / 100)
    else:
        expense -= (expense * 5 / 100)
    return expense


def total_cost_B(flour):
    expense = flour * 31000
    if flour < 40:
        expense -= (expense * 5 / 100)
    else:
        expense -= (expense * 10 / 100)
    return expense


def round_up(flour):
    if flour % 2 == 0:
        return flour
    return (flour // 2) * 2 + 2


def flour_order(large_thick, large_thin, medium_thick, medium_thin):
    """
    Decide to order from store A or B
    :param large_thick:
    :param large_thin:
    :param medium_thick:
    :param medium_thin:
    :return: total flour, selected provider and total cost
    """
    flour = int(round_up(total_flour(large_thick, large_thin, medium_thick, medium_thin)))
    ex_A = int(total_cost_A(flour))
    ex_B = int(total_cost_B(flour))
    print(
        f'We need to order {flour}kg of flour, which costs {ex_A}VND if we buy from A and {ex_B}VND if we buy from B.')
    if ex_A <= ex_B:
        return flour, "A", ex_A
    return flour, "B", ex_B


def main():
    total_flour_in_kg, decision, total_cost = flour_order(10, 30, 10, 50)
    print(total_flour_in_kg)
    print(decision)
    print(total_cost)


main()
