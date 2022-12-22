#!/usr/bin/python3
"""
Pascal triangle module
"""


def pascal_triangle(n):
    """
    Returns a list of lists of intergers representing
    the Pascal's triangle of n
    """

    if type(n) is int:
        triangle = []
        if n <= 0:
            return triangle
        else:
            prev = [1]
            for row in range(n):
                a_list = []
                if row == 0:
                    a_list = [1]
                else:
                    for i in range(row + 1):
                        if i == 0:
                            a_list.append(prev[i])
                        elif i == (row):
                            a_list.append(prev[i - 1])
                        else:
                            a_list.append(prev[i - 1] + prev[i])
                prev = a_list
                triangle.append(a_list)
            return triangle
