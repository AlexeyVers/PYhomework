numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []
is_prime = True
includes = []
for i in numbers:
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime:
        if i == 1:
            includes.append(i)
        else:
            primes.append(i)
    else:
        not_primes.append(i)

print('Простые: ', primes, 'Не простые: ', not_primes)
