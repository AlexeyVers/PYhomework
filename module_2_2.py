first = input('Первое число: ')
second = input('ВТорое число: ')
third = input('Третье число: ')

if first == second and second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)
