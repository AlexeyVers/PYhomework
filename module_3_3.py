def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b=25, c=[1,2,3])
print_params()

values_list = ['tetx', 6, False]
values_dict = {'a': 3, 'b': 'long', 'c': False}

print_params(*values_list)
print_params(*values_dict)
print_params(**values_dict)

values_list_2 =[[1, 2, 3], 'some text']
print_params(*values_list_2, 4)
