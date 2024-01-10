#!/usr/bin/python3
def search_replace(my_list, search, replace):
    updated_list = list(my_list)

    for match in range(len(my_list)):
        if updated_list[match] == search:
            updated_list[match] = replace

return updated_list
