def sort_list(list):

    for x in range(len(list)-1,0,-1):
        for s in range(x):
            if list[s] > list[s+1]:
                temp = list[s]
                list[s] = list[s+1]
                list[s+1] = temp

    return list

list = [2, 8, 5, 7, 12, 10, 4]
print(sort_list(list))