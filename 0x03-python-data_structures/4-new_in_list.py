#!usr/bin/python3
def new_in_list(my_list, idx, element):
    a = len(my_list) - 1
    if (idx < 0) or (idx > a):
        return my_list
    else:
        new_list = my_list.copy
        new_list[idx] = element
        return new_list
