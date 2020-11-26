
import numpy as np

def game_core(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    min_number = 1
    max_number = 100
    count = 1
    predict = np.random.randint(min_number, max_number+1)

    while predict != number:
            count += 1
            if number > predict:
                min_number = predict+1
            elif number < predict:
                max_number = predict

            predict = (min_number + max_number) // 2

    return(count)

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))

    for number in random_array:
        count_ls.append(game_core(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    
    return(score)

score_game(game_core)
