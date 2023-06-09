'''
Задача 444
Лотерея круглого стола

Группа из p людей решила сесть за круглый стол и разыграть игру с обменом лотерейными билетами. Каждый игрок начинает со случайно назначенным нестертым лотерейным билетом. При стирании защитного покрытия на каждом билете становится виден его выигрыш - целое количество фунтов стерлингов между £1 и £p, причем все билеты имеют разный выигрыш. Цель игры для каждого игрока - получить как можно больший выигрыш на момент покидания игры.
Случайный человек выбирается первым игроком. Далее игроки ходят по кругу, каждый игрок в свой ход может выбрать одно из двух:
1. Игрок стирает покрытие на своем билете и показывает его выигрыш всем сидящим за столом.
2. Игрок может обменять свой нестертый билет на стертый билет предыдущего игрока и покинуть игру с этим билетом. Предыдущий игрок тогда стирает покрытие с полученного билета и показывает его выигрыш всем сидящим за столом.
Игра завершается, когда все билеты стерты. Все игроки, остающиеся за столом, должны покинуть игру с имеющимся на руках билетом.
Предположим, что каждый игрок следует оптимальной стратегии для максимизирования ожидаемого выигрыша его билета. 
Пусть E(p) будет ожидаемым числом игроков, остающихся за столом на момент завершения игры, при общем количестве игроков равным p (например, E(111) = 5.2912 при округлении до 5 значимых цифр).
Пусть S1(N) =  E(p)
Пусть Sk(N) =  Sk-1(p) для k > 1
Найдите S20(1014) и запишите ответ в стандартном виде округленным до 10 значимых цифр. Используйте строчную латинскую букву "e", чтобы отделить мантиссу от порядка (например, S3(100) = 5.983679014e5).
 Оригинал
'''