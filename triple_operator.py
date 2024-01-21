import random
numbers = []
for i in range(10):
    numbers.append(random.randint(a=0,b=10))
print(numbers)
print('Число 13 есть в вашем списке') if 13 in numbers else print('Числа 13 нет в вашем списке')
result = None
if 4 in numbers:
    result = 'Есть китайское несчастливое число'
else:
    result = 'Все окей'
print('Результат выражения:\n', result)
result = 'Есть китайское несчастное число' if 4 in numbers else 'Все окей'
print('Результат вражения:\n', result)