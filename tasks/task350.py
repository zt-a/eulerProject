'''
Задача 350
Границы наименьшего большего и наибольшего меньшего

Списком длинною n является последовательность из n натуральных чисел.
Примеры таких списков: (2,4,6), (2,6,4), (10,6,15,6) и (11).

Наибольший общий делитель, сокращенно НОД, такого списка - наибольшее натуральное число, на которое делится каждая запись списка.
Примеры: НОД(2,6,4) = 2, НОД(10,6,15,6) = 1 и НОД(11) = 11.

Наименьшее общее кратное, сокращенно НОК, такого списка - наименьшее натуральное число, которое делит без остатка каждую запись списка. 
Примеры: НОК(2,6,4) = 12, НОК(10,6,15,6) = 30 и НОК(11) = 11.

Пусть f(G, L, N) - количество списков длинною N, у которых НОД ≥ G и НОК ≤ L. Например:

f(10, 100, 1) = 91.
f(10, 100, 2) = 327.
f(10, 100, 3) = 1135.
f(10, 100, 1000) mod 1014 = 3286053.

Найдите f(106, 1012, 1018) mod 1014.

 Оригинал
'''