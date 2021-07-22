import numpy as np


def score_game(game_core):
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array :
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


def game_core_v1(number):
    count = 1  # Начало счетчика попыток
    predict = 50  # Предсказываем среднее число из диапозона 1-101, для удобства поиска числа.
    if number % 2 == 0:  # Пишем условия для проверки четности числа
        while number != predict:  # Если условие срабатывает то прибавляем плюс один к числу попыток
            count += 1
            if number > predict:  # Если загаданое число больше предполагамеого то прибавляет 2, так как число четное
                predict += 2
            elif number < predict:  # Иначе вычитаем 2
                predict -= 2
    elif number % 2 != 0:  # Если число нечетное то прибавляем или вычитаем 1
        while number != predict:
            count += 1
            if number > predict:
                predict += 1
            elif number < predict:
                predict -= 1
    return count  # Возвращаем количество попыток


score_game(game_core_v1)
