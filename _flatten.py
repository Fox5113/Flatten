#!/bin/python3


def flat_list(array, new_list=None):
    if new_list is None:
        new_list = []
    for i in array:
        if type(i) == int:
            new_list.append(i)
        else:
            flat_list(i, new_list)
    return new_list



if __name__ == '__main__':
    arr = input()
    print(flat_list(arr))