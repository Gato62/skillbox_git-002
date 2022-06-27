from factorial import factorial_num as f


def summa(a, b):
    return a + b


num_one, num_two = int(input('Enter first 1: ')), int(input('Enter second 1: '))

total = summa(num_one, num_two)

result = f(total)

print(f'result = {result}')
