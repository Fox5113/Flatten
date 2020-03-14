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
    A = [1, 2, [3, 4, [5, 6], 7], [8, [9, [10]]]]
    B = [[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]
    C = [1, 2, 3]
    D = []
    print(flat_list(A))
    print(flat_list(B))
    print(flat_list(C))
    print(flat_list(D))