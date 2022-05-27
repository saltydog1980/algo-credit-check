import functools
def credit_check(string):
    #creating base list by taking map over the string converting to in and casting to list
    base_list = list(map(int,string))
    #for looping over the base list by 2
    for x in range(0, len(base_list), 2):
        #if num *2 over single digit
        if base_list[x]*2 > 9:
            #creating variable nums by taking the num *2 to string so I can map/list it to break into a list with ints being each digit 
            nums = list(map(int, str(base_list[x]*2)))
            #creating variable fin by taking the nums list and reducing it
            fin = functools.reduce(lambda agg, item : agg + item, nums)
            #re-assigning fin to the original nums index in the base list
            base_list[x] = fin
        else:
            #if single digit just doubling and re-assigning to the same index in base list
            base_list[x] = base_list[x]*2
    #Rapheal's favorite. Had to do a ternary assigning the out put to variable a so that if the reduce of the list % 10 was 0 a is valid else invalid
    a = 'The number is valid!' if functools.reduce(lambda agg, item : agg + item, base_list) % 10 == 0 else 'The number is invalid!'
    #returning variable a
    return a