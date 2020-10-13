import math


def func1(x, y):
    return tuple((x + y, x * y))


def func2(x, y):
    return math.sqrt(x + math.sqrt(y))


def func3():
    list_www = []
    for i in range(1000, 4250):
        if i % 5 == 0 and i % 3 != 0:
            list_www.append(i)
    print(list_www)


def func4(x):
    if x in range(3, 6):
        x -= 13
    elif x in range(8, 41):
        x -= 50
    elif 0 > x > 2000:
        x *= 4
    else:
        x = 0
        return x


def func5(x):
    return (x * 1.8) + 32


def func6(money, intrest):
    return money * (intrest / 100) * 5


def func7(week, month, year):
    days = week * 7 + month * 30 + year * 360
    return days


def func8(x):
    i = 2
    list_a = []
    while i * i <= x:
        if x % i:
            i += 1
        else:
            x //= i
            list_a.append(i)
    if x > 1:
        list_a.append(i)
        return list_a


def func9(x):
    y = []
    for i in range(1, x + 1):
        if x % i == 0:
            y.append(i)
    return y


print(func9(36))


def func10(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


print(func10(0, 0, 1, 1))


def func11(x):
    nums = []
    elem = 0
    sequence = 0
    while elem < x:
        elem = sequence ** 2
        if elem < x:
            nums.append(elem)
            sequence += 1
        else:
            break
    return nums


def func12(lis_a, coord):
    x = coord[0]
    y = coord[1]
    sum_elem = 0
    for i in range(x, y + 1):
        sum_elem += lis_a[i]
        return sum_elem


def func13(x, y):
    list_a = []
    for i in range(x):
        list_a.append(y)
    return list_a


print(func13(6, -1))


def func14(arr, rem):
    return arr.remove(rem)




def func15(digit):
    listdigit = list(map(int, str(digit)))
    maxi = listdigit.index(max(listdigit))
    mini = listdigit.index(min(listdigit))
    listdigit[max], listdigit[min] = listdigit[min]
    return int(''.join(str, listdigit))


def func16(num):
    array = list(map(int, str(num)))
    flag = False
    for elem in range(len(array) - 1):
        if max(array[elem], array[elem + 1]) == array[elem]:
            flag = True
        else:
            flag = False
            break
    return flag


def func17(some_list):
    return some_list == some_list[::-1]


def z18(*args, string):
    return ' '.join([word for word in string.split() if not any(letter in word for letter in args)])


def func19(ip):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        return False
    else:
        return True


def func20(string):
    digits = set("0123456789")
    only_digits = ""
    for digit in string:
        if digit in digits:
            only_digits += digit
    return only_digits


def func21(*args):
    even = 0
    odd = 0
    for elem in args:
        if elem % 2 == 0:
            even += elem
        else:
            odd += elem
    return even / 2, odd / 2


def func22(array):
    return [elem for elem in array if elem != 0]


def func23(array, some_int):
    blizayshee = 10000
    for elem in array:
        blizayshee = min(blizayshee, abs(elem - some_int))

    for i in array:
        if abs(i - some_int == blizayshee):
            return i


def func24(predlozheniye):
    vowels = set("аоуеияёэю")
    new_string = ""
    for letter in predlozheniye:
        if letter in vowels:
            new_string += letter + 'c' + letter
        else:
            new_string += letter

    return new_string

def func26(array):
    some_map = {}
    for i in array:
        some_map.update({i: list(array).count(i)})
    some_list = some_map.values()
    for elem in some_list:
        if elem > 1:
            return False
        else:
            return True


def func27(array):
    counter = 0
    arr_max = max(array)
    for elem in array:
        if elem * 0.1 <= arr_max:
            counter += 1
    return counter

def func34(digit):
    months = {1: "December", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
              9: "September", 10: "November", 11: "October", 12: "December"}
    return months.get(digit)


def func35(digit):
    season = {1: "Winter", 2: "Winter", 3: "Spring", 4: "Spring", 5: "Spring", 6: "Summer", 7: "Summer", 8: "Summer",
              9: "Autumn", 10: "Autumn", 11: "Autumn", 12: "Winter"}
    return season.get(digit)


def func36(list1, list2):
    return dict(zip(list1, list2))
