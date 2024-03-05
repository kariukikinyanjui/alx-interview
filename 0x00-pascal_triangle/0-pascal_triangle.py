#!/usr/bin/python3
"""Generate Pascal's triangle up to the nth row"""


def pascal_triangle(n):
    """Returns an empty list in n <= 0"""
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle


def print_triangle(triangle):
    """Print the triangle"""
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
