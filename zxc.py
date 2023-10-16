pythonexpression = input("Введите арифметическое выражение: ")
# Разделяем выражение на два числа и операцию
num1, operation, num2 = expression.split()

num2 = float(num2)

    result = num1 + num2elif operation == '-':
    result = num1 - num2elif operation == '*':
    result = num1 * num2elif operation == '/':
    result = num1 / num2else:
    print("Некорректная операция")    exit()










import random

# Создаем список случайных чисел
numbers = [random.randint(-10, 10) for i in range(10)]

# подсчет количества отрицательных, положительных и нулевых элементов
negatives = 0
positives = 0
zeros = 0

#  переменные для хранения минимального и максимального элементов
min_num = numbers[0]
max_num = numbers[0]

# Проходим по списку чисел и выполняем необходимые операции
for num in numbers:
    if num < 0:
        negatives += 1
    elif num > 0:
        positives += 1
    else:
        zeros += 1
        
    if num < min_num:
        min_num = num
        
    if num > max_num:
        max_num = num

# Выводим результаты на экран
print(f"Список чисел: {numbers}")
print(f"Минимальный элемент: {min_num}")
print(f"Максимальный элемент: {max_num}")
print(f" отрицательное: {negatives}")
print(f" положительное : {positives}")
print(f"Количество нулей: {zeros}")
