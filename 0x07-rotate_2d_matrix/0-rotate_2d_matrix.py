#!/usr/bin/env python3
""" rotate matrix module """


def rotate_2d_matrix(matrix):
    """ Rotate a n X n to 90 degrees clockwise """
    x = len(matrix[0])

    for i in range(x - 1, -1, -1):
        for j in range(0, x):
            matrix[j].append(matrix[i].pop(0))
