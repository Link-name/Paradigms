""" Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки. """
""" императивном стиле """
def sort_list_imperative(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] < numbers[j + 1]:
                # Обмен значениями, если текущий элемент меньше следующего
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp

# Пример использования:
numbers = [64, 34, 25, 12, 22, 11, 90]
sort_list_imperative(numbers)
print("Отсортированный в порядке убывания список:", numbers)


""" декларативном стиле """
def sort_list_declarative(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers

# Пример использования:
my_numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = sort_list_declarative(my_numbers)
print("Отсортированный в порядке убывания список:", sorted_numbers)
