#!/usr/bin/python3
"""A function that divides element by element 2 lists.

Parameters:
    @my_list_1: a given list
    @my_list_2: a given list
    @list_lenght: given lenght
Return:
    - A new list (lenght = list_lenght) with all divisions
Description:
    - list_lenght can be bigger than the lenght of both lists
    - If 2 elements cant be divided, the result is 0
    - If an element is not an integer or float, it prints: wrong type
    - If the division can't be done,  it prints: division by 0
    - If my_list_1 or my_list_2 is too shoet, it prints: out of range
    - No modules should be imported
"""


def list_division(my_list_1, my_list_2, list_length):
    new_list = [0] * list_length
    for i in range(list_length):
        try:
            division = (my_list_1[i]) / (my_list_2[i])
            new_list[i] = division
        except (TypeError, ValueError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            pass
    return new_list
