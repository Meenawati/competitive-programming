def selection_sort(list):
    for i in range(len(list)-1):
        min_ele_index = i
        for j in range(i+1, len(list)):
            if list[min_ele_index] > list[j]:
                min_ele_index = j

        temp = list[i]
        list[i] = list[min_ele_index]
        list[min_ele_index] = temp

    return list


list = [2, 5, 1, 8, 9, 3, 10]
print(selection_sort(list))