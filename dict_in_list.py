# Write a Python program to check if all dictionaries in a list are empty or not


def dict_in_list(lst):
    for d in lst:
        if type(d) is not dict:
            print("All Elements of list are not dictionary")
            return False
        elif d:
            return False
    return True


print(dict_in_list([{}, {}, {}])) # returns True
print(dict_in_list([{}, {1, 2}, {}])) # prints All Elements of list are not dictionary and returns False
print(dict_in_list([{}, {1: 'one', 2: 'two'}, {}])) # returns False