import functools
def credit_check(string):
    base_list = list(map(int,string))
    for x in range(0, len(base_list), 2):
        if base_list[x]*2 > 9:
            nums = list(map(int, str(base_list[x]*2)))
            fin = functools.reduce(lambda agg, item : agg + item, nums)
            base_list[x] = fin
        else:
            base_list[x] = base_list[x]*2
    a = 'The number is valid!' if functools.reduce(lambda agg, item : agg + item, base_list) % 10 == 0 else 'The number is invalid!'
    return a