from collections import Counter
import codecs
import re


def math_wait(value: list, probability: list) -> float:
    """
    Математическое ожидание дискретной величины
    :param value: список значений
    :param probability: список соответствующих значениям вероятностей
    :return: M[x]
    """
    return sum([x * p for x, p in zip(value, probability)])


def regular_count(sequence: str, not_summary: bool = True, *symbols: str) -> Counter():
    """
    sequence : символьная последовательность без пробелов (исходные данные)
    :param symbols: символы, на основе которых будет осуществляться поиск под-последовательностей
    :param not_summary: True - считать количество элементов для каждой подпоследовательности
    False считать только колличество элементов в подпоследовательности
    :return: соотношение подпоследовательность(ключ) количество совпадений(значение) в виде словаря Counter
    """
    if not_summary:
        return Counter(re.findall('|'.join([f'[{s}]*[{s}]' for s in symbols]), sequence))
    else:
        return Counter([len(seq) for seq in re.findall('|'.join([f'[{s}]*[{s}]' for s in symbols]), sequence)])


def predict(length: int, n: int) -> float:
    """
    Предсказание количества идущих подряд символов для последовательности с известной длинной
    :param length: длинна последовательности
    :param n: количество символов, следующих подрад, для котогоко делаем предсказание
    :return: средняя вероятности встретить под последовательности длинной n в последовательности length
    """
    if length < 0 or n < 0:
        raise ValueError
    return length/2**(n+1)


def limit_series(length: int, predicate, index: int = 0) -> {int, float}:
    """
    Ряд Nn ограниченный условием
    :param predicate: функция - условие ограничения ряда
    :param length: количество элементов в рассматриваемой последовательности
    :param index: минимальная длина пол-последовательности символов, для которой будет рассчитана вероятности
    :return:
    """
    if length < 0 or index < 0:
        raise ValueError
    temporal = {}
    while True:
        step = predict(length, index)
        if predicate(step):
            temporal[index] = step
            index += 1
        else:
            return temporal


if __name__ == '__main__':
    # border_func = lambda x: x >= 1
    # print(limit_series(100, border_func, 0))
    # Парсим файл с исходными данными
    simple_parser = {}
    with codecs.open('C:/Users/RTFE4/Desktop/ИТАСУ/ИВТ/2 Семестр/Специальные главы математики часть 2/ДЗ/ДЗ8/0and1.txt',
                     'r', 'utf-8') as reader:
        temp = []
        for i in reader:
            temp.append(i)
            if len(temp) == 2:
                value = temp.pop()
                name = temp.pop()
                simple_parser[name.partition('\r')[0]] = re.sub('[\[\],]', '', value.partition('\r')[0])
    # Получить предсказание для каждой последовательности
    for i, j in simple_parser.items():
        print(f"Выборка: {i}")
        print(limit_series(len(j), lambda x: x >= 1, 1))
    print("Экспертные")
    # Получить эксперементальные значения для последовательности
    for i, j in simple_parser.items():
        print(f"Выборка: {i}")
        print(regular_count(j, False, '0', 1))