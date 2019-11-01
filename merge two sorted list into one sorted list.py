# merge two sorted list and return 3rd sorted list


def merge_two_sorted_lists(list1, list2):
    list3 = []

    j = 0
    i = 0
    while i < len(list1):
        if j < len(list2):
            # if both list contains same element then add only one
            if list1[i] == list2[j]:
                list3.append(list1[i])
                j += 1
                i += 1

            elif list1[i] < list2[j]:
                list3.append(list1[i])
                i += 1

            else:
                list3.append(list2[j])
                j += 1
        else:
            list3.append(list1[i])
            i += 1

    while j < len(list2):
        list3.append(list2[j])
        j += 1

    return list3


list1 = [2, 9, 11, 12, 18, 24, 25]
list2 = [1, 4, 5, 9, 12, 15, 19]
print(merge_two_sorted_lists(list1, list2))

list1 = [2, 9, 11, 12]
list2 = [1, 4, 5, 9, 12, 15, 19]
print(merge_two_sorted_lists(list1, list2))

