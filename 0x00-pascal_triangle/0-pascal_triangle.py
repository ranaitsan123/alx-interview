#!/usr/bin/python3
def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle of n.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list: A list of lists containing the values of Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)  # Initialize the row with 1s
        for j in range(1, i):  # Calculate the values for the current row
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
