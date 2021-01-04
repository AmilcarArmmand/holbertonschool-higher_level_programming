#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for item in range(0, list_length):
        try:
            result = my_list_1[item] / my_list_2[item]
        except TypeError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)
    return (new_list)
