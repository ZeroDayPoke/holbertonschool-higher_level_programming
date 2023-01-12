#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for iteri in range(len(matrix)):
        for iterj in range(len(matrix[iteri])):
            print("{:d}".format(matrix[iteri][iterj]), end="")
            if iterj != len(matrix[iteri]) - 1:
                print(" ", end="")
        print()
