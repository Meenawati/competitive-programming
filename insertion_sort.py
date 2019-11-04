def insertion_sort(list):
    for i in range(1,len(list)):
        current_ele = list[i]
        cur_ele_index = i
        while current_ele < list[cur_ele_index-1] and cur_ele_index > 0:
            list[cur_ele_index] = list[cur_ele_index-1]
            cur_ele_index = cur_ele_index-1
        list[cur_ele_index] = current_ele
    return list


list = [8, 2, 7, 6, 5, 1]
print(insertion_sort(list))