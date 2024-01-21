import random
chars = 'abcdef'
numbers = []
for i in range(10):
    numbers.append(random.randint(a=0,b=10))
print(numbers)
print('Число 44 есть в вашем списке') if 44 in numbers else print('Числа 44 нет в вашем списке')
print('Число 44 есть в вашем списке' if 44 in numbers else 'Числа 44 нет в вашем списке')