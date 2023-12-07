""" Корреляция
● Контекст
Корреляция - статистическая мера, используемая для оценки
связи между двумя случайными величинами.
● Ваша задача
Написать скрипт для расчета корреляции Пирсона между
двумя случайными величинами (двумя массивами). Можете
использовать любую парадигму, но рекомендую использовать
функциональную, т.к. в этом примере она значительно
упростит вам жизнь """

from functools import reduce

def mean(values):
    return sum(values) / len(values)

def pearson_correlation(x, y):
    mean_x = mean(x)
    mean_y = mean(y)

    numerator = sum([(x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x))])
    denominator_x = sum([(x[i] - mean_x)**2 for i in range(len(x))])
    denominator_y = sum([(y[i] - mean_y)**2 for i in range(len(y))])

    correlation = numerator / ((denominator_x * denominator_y)**0.5)
    return correlation

# Пример использования
if __name__ == "__main__":
    # Ваши два массива данных
    array1 = [1, 2, 3, 4, 5]
    array2 = [2, 3, 4, 5, 6]

    # Расчет корреляции
    correlation = pearson_correlation(array1, array2)

    # Вывод результата
    print(f"Корреляция Пирсона: {correlation}")


""" _________________________ """
from functools import reduce

def mean(values):
    return sum(values) / len(values)

def covariance(X, Y):
    n = len(X)
    mean_X, mean_Y = mean(X), mean(Y)
    return sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(n))

def correlation(X, Y):
    covar = covariance(X, Y)
    std_dev_X = (covariance(X, X)) ** 0.5
    std_dev_Y = (covariance(Y, Y)) ** 0.5
    return covar / (std_dev_X * std_dev_Y)

def main():
    # Пример данных - два массива значений
    array1 = [1, 2, 3, 4, 5]
    array2 = [5, 4, 3, 2, 1]

    # Расчет корреляции Пирсона
    corr = correlation(array1, array2)

    print(f"Массив 1: {array1}")
    print(f"Массив 2: {array2}")
    print(f"Корреляция Пирсона: {corr}")

if __name__ == "__main__":
    main()
