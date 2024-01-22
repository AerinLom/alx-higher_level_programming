#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for pos in range(list_length):

        try:
            list_div = my_list_1[pos] / my_list_2[pos]

        except ZeroDivisionError:
            print("division by 0")
            list_div = 0

        except TypeError:
            print("wrong type")
            list_div = 0

        except IndexError:
            print("out of range")
            list_div = 0

        finally:
            result_list.append(list_div)

    return result_list
