#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for iteri in matrix:
        for iterj in iteri:
            print("{:d}".format(iterj), end=" ")
        print()
