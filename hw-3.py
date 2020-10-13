lst = [4, 5, 6, 7, 8, 9, 0]


def shift(lst, steps):
    new_list = []
    if steps < 0:
        new_list += lst[-steps:]
        new_list += lst[:-steps]
        return new_list
    new_list += lst[-steps:]
    new_list += lst[:-steps]

    return new_list


print(shift(lst, -2))


def has_equal_diff(array):
    boole = True
    for i in array:
        if i % array[0] == 0:
            boole = True
        else:
            return False
    return boole


def intersection(x, y, new_type):
    for i in x:
        for j in y:
            if i == j:
                new_type.append(i)
                break
    return new_type
