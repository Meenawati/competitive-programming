# when element is not present in the list return -1 otherwise return index of list


def binary_search(list, n):
    if len(list) == 0:
        return -1

    start = 0
    end = len(list) - 1

    while start <= end:
        mid = start + int((end - start)/2)
        if list[mid] == n:
            return mid
        elif list[mid] < n:
            start = mid + 1
        else:
            end = mid - 1
    return -1


list1 = [2, 5, 13, 34, 56, 90, 345, 560, 678]
list2 = [2, 5, 13, 34, 56, 90, 345, 560, 678, 900]
print(binary_search(list1, 13))
print(binary_search(list1, 15))
print(binary_search(list2, 678))
print(binary_search(list2, 15))
print(binary_search([], 5))