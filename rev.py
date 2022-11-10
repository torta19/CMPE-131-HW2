def reverse_list(some_list): 
    #method using for loop
    if len(some_list) == 0:
        return None
    else:
        list_size = len(some_list) - 1
        b = [some_list[i] for i in range(list_size, -1, -1)]
        return b


