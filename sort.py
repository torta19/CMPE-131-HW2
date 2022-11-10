def sort_dictionary(some_dict):
    items = list(some_dict.items())
    for i in range(1, len(items)):
        key = items[i][1][1] 
    
        current_item = items[i]
        '''since we have a list of tuples with the second item is a tuple and 
        we want to compare the second item we use [1][1]'''
        j = i - 1
        while j >= 0 and key < items[j][1][1]:
            items[j+1] = items[j]
            j -= 1

        items[j+1] = current_item
    
    sorted_list = [(x[0], x[1][0]) for x in items]
    
    return sorted_list