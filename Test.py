def merge_list(list_to_merge):
    new_list = []
    for x in range(len(list_to_merge)):
        new_list.extend(list_to_merge[x])
    return new_list


print(merge_list([[1, 8, 3], [-5, 0], [4], [2, 3, 3]]))


def multi_power(orignal, powers):
    new_list = []
    for i in range(len(orignal)):
        new_list.append(orignal[i]**powers[i])
    return new_list


print(multi_power((3, 2, 0, -2, -7), (1 / 3, 7, 10, -2, 3)))


def rm_elems(list_a):
    list_b = []

    for line in list_a:
        list_b.append([])
        print(list_b)
        for elem in line:
            for line_2 in list_b:
                if elem in line_2:
                    break
            else:
                list_b[-1].append(elem)
    return list_b


print(rm_elems([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]))


def expand(unchangeablee, index = None, expanby = None):
    new_list = []
    for i in range(len(unchangeablee)):
        new_list.append(unchangeablee[i])
        print(new_list)
        if i == index:
            for elem in expanby:
                new_list[i].append(elem)
    return tuple(new_list)


print(expand(([1, 2], [3, 4], [5, 6]), index = 2, expanby = [99, 0]))



