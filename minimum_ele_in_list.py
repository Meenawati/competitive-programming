def min_ele_in_list(list):
    min_ele = list[0]
    for i in range(1,len(list)):
        if min_ele > list[i]:
            min_ele = list[i]

    return min_ele


list = [2, 6, 8, 1, 5]
print(min_ele_in_list(list))

