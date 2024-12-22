def myfun(lst):
    if not lst:
        return []
    return [lst[-1]] + myfun(lst[:-1])

lst = [3,2,1]
print(myfun(lst))