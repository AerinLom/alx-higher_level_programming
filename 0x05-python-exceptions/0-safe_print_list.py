#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for index in range(x):
            print("{}".format(my_list[index]), end="")
            counter += 1

    except (IndexError, TypeError):
        pass

    finally:
        print()
    return counter
