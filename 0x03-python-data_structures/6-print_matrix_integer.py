#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
        return
    for row in matrix:
        x = list(" " * (len(row) - 1))
        x.append("\n")
        y = zip(row, x)
        for t in y:
            print("{:d}{:c}".format(t[0], ord(t[1])), end="")
            
