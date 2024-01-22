#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    counter = 0

    for indexNum in range(x): 
        try:
            data = my_list[indexNum]
            if isinstance(data, int):
                print("{}".format(my_list[indexNum]), end="")
                counter += 1
        except (ValueError, TypeError):
            pass
    print()
    return counter
