# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 1
# Author: Nguyen Nguyen Khuong (s3924577)
# Created date: 15/11/2021
# Last modified date: 16/11/2021


import random


def find_split_80(integer_list):
    """ Sort the list and return the 17th number
    :param integer_list:
    :return: the 16th number in sorted list
    """
    # Because after sorting, the 17th number of list always meet the requirement
    # Return the 16th number in sorted list (because the list starts at 0)
    integer_list.sort()
    split_80 = integer_list[16]
    return split_80


def generate_random_list(List):
    """
    :param List:
    :return: generate a random list with 20 numbers
    """
    for i in range(20):
        x = random.randint(1, 100)
        List.append(x)


def print_list(integer_list):
    """
    :param integer_list:
    :return: print a list out
    """
    for i in range(20):
        print(integer_list[i], end=' ')
    print("\n", end='')


def main():
    List = []
    generate_random_list(List)
    print_list(List)
    print(find_split_80(List))


main()

