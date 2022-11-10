def swap_list(some_list):
    #swap middle element with the last element 
    if not len(some_list) <= 1:
       middle = int((len(some_list)-1)/2)
       last = len(some_list) - 1
       some_list[middle], some_list[last] = some_list[last], some_list[middle]

    return some_list

    