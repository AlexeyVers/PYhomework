
def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result % 2:
            return 'Чётное'
        else:
            return 'Не чётное'
    return wrapper

@is_prime
def sum_three(*number):
    result = sum(number)
    return result

result = sum_three(2, 3, 3)
print(result)
