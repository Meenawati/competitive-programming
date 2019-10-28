# Question: find if ALL the numbers in a given list of integers are PART of the series defined by the following.
# f(0) = 0 f(1) = 1 f(n) = 2*f(n-1) - 2*f(n-2) for all n > 1

def is_part_of_series(lst):
    lst.sort()
    last_number = lst[len(lst) - 1]
    given_series = series(last_number)
    for i in lst:
        if i not in given_series:
            return False
    return True

def series(n):
    a = 0
    b = 1
    li = [a, b]
    for i in range(2, n):
        c = 2*(a + b)
        a = b
        b = c
        li.append(c)
    print(li)
    return li