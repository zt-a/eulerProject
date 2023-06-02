'''
Задача 499
Петербургская лотерея

Азартный игрок решил поучаствовать в особой лотерее. Она состоит из одной или нескольких игр.
Каждая игра стоит m фунтов стерлингов и начинается с банком в 1 фунт. Игрок бросает симметричную монету. Каждый раз, когда выпадает решка, банк удваивается и игра продолжается. Если выпадает орел, игра завершается и игрок забирает все деньги, имеющиеся в банке на тот момент. Игрок точно выиграет как минимум 1 фунт (начальный банк), потратив m фунтов (цена начала игры).
Игрок не может продолжать игру, если у него остается меньше m фунтов.
Пусть pm(s) обозначает вероятность того, что у игрока никогда не кончатся деньги при игре в эту лотерею с его начальным капиталом в s фунтов и ценой каждой игры в m фунтов.
Например, p2(2) ≈ 0.2522, p2(5) ≈ 0.6873 и p6(10 000) ≈ 0.9952 (заметьте: pm(s) = 0 для s < m).
Найдите p15(109) и дайте ответ округленным до 7 знака после десятичной точки в виде 0.abcdefg.
 Оригинал
'''