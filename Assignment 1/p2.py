# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 1
# Author: Nguyen Nguyen Khuong (s3924577)
# Created date: 15/11/2021
# Last modified date: 16/11/2021


import math
import random


def is_inside_circle(x, y):
    a_num = math.sqrt(x * x + y * y)
    if a_num > 1:
        return False
    return True


def generate_N_random_points(N):
    """
    Generate a list of N random points
    :param N: size of list
    :return: the number of points which inside the circle
    """
    inside = 0
    for i in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if is_inside_circle(x, y):
            inside += 1
    return inside


def estimate_pi(N):
    """
    Caculate estimated pi base on N random points
    :param N: size of list
    :return: estimated pi
    """
    inside = generate_N_random_points(N)
    estimated_pi = 4 * inside / N
    return estimated_pi


def main():
    print(estimate_pi(1000))


main()
