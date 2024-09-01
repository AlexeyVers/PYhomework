my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count = len(my_list)
static_count = 0
while static_count < count:
    if my_list[static_count] > 0:
        print(my_list[static_count])
        static_count = static_count + 1
    else:
        static_count = static_count + 1
