# traversal
tree = {
    'root_1': [1, 2, 3],
    'root_2': {
        'child_1': [4, 5],
        'child_2': {
            'grandchild_1': [6, 7, 8],
            'grandchild_2': {
                'great_grandchild_1': [9],
                'great_grandchild_2': [10, 11]
            }
        }
    },
    'root_3': [12, 13],
    'root_4': {
        'child_1': [14],
        'child_2': {
            'grandchild_1': [15, 16],
            'grandchild_2': {
                'great_grandchild_1': [17, 18, 19, 20]
            }
        }
    },
    'root_5': [21]
}


# second time [1,2,3, 4,5 ]
def get_obj_sum(obj, target_list=None):
    target_list = [] if target_list is None else target_list
    for key in obj:
        if type(obj[key]) == list:
            target_list.extend(obj[key])
        else:
            get_obj_sum(obj[key], target_list)
    return sum(target_list)


print('*' * 20)
print(get_obj_sum(tree))
print('*' * 20)
