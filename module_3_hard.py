data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

sum_all = 0
def calculate_structure_sum(list_):
    global sum_all
    for i in range(len(list_)):
        if isinstance(list_[i], str):
            sum_all += len(list_[i])
        elif isinstance(list_[i], int):
            sum_all += int(list_[i])
        elif isinstance(list_[i], dict):
            calculate_structure_sum([*list_[i].items()])
        elif isinstance(list_[i], list) or isinstance(list_[i], tuple):
            calculate_structure_sum(list_[i])
        elif isinstance(list_[i], set):
            calculate_structure_sum([*list_[i]])
    return sum_all


print(calculate_structure_sum(data_structure))
