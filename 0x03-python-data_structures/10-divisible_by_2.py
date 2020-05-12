#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    even_multiples = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            even_multiples.append(True)
        else:
            even_multiples.append(False)
    return (even_multiples)
