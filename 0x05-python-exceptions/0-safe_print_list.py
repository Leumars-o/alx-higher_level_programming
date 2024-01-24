#!/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for elements in my_list:
            if count < x:
                print(my_list[count], end="")
                count += 1
            else:
                break
    except IndexError:
        None
    print()
    return (count)
