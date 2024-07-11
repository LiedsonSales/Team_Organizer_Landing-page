list_1 = [1, 2, 3, 4, 5, 6, 7]
List_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def zipper(one, two):
    size = list_longest(one, two)
    result = [
        one[c] + two[c]
        for c in range(0, len(size))
    ]

    return result


def list_longest(l_01, l_02):
    if len(l_01) >= len(l_02):
        return l_02
    
    else:
        return l_01
    
# print(list_size(list_1, List_2))
print(zipper(list_1, List_2))