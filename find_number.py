import numpy as np


def score_game(game_core):
    '''запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1) #фиксируем random seed, чтобы эксперимент был воспроизводим
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score



def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
    #Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    n_max = 100
    n_min = 0
    predict = np.random.randint(1,101)
    while predict != number:
        count+=1
        if number < n_max - (n_max-n_min)/2:
            n_max = n_max - (n_max-n_min)/2
            predict = int(n_max)
        elif number > n_max - (n_max-n_min)/2:
            n_min = n_min + (n_max-n_min)/2
            predict = int(n_min)
        else:
            break

    return(count) # выход из цикла, если угадали



score_game(game_core_v2)
