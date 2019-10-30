# Question: find if ALL the numbers in a given list of integers are PART of the series defined by the following.
# f(0) = 0 f(1) = 1 f(n) = 2*f(n-1) - 2*f(n-2) for all n > 1

def is_part_of_series(list):
    # corner case: list is empty then show user message and return false
    if len(list) == 0:
        print("Empty list provided. Please provide list with some numbers")
        return False

    # sort the list and find the absolute large value to find up-to where the series can extend
    list.sort()
    n = 0
    if abs(list[0]) < list[-1]:
        n=list[-1]
    else:
        n = abs(list[0])

    series = get_series(n)

    # check whether items of list are present in series
    for item in list:
        if item not in series:
            return False
    return True

# function to generate the series where n is used as
# reference for extending the series up-to certain limit
def get_series(n):
    series = [0,1]
    a = 0
    b = 1
    c = 2 * (b - a)
    series.append(c)
    while abs(c) <= n:
        a = b
        b = c
        c = 2 * (b - a)
        series.append(c)
    print(series)
    return series
