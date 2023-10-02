def complex_list_sum(list_):
    curr_sum = 0
    for el in list_:
        curr_sum += complex_list_sum(el) if type(el) is list else el
    return curr_sum
