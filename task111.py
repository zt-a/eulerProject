'''
Задача 111
Простые числа с повторениями

Рассматривая четырехзначные простые числа с повторяющимися цифрами, становится очевидным, что все цифры не могут быть одинаковыми: 1111 делится без остатка на 11, 2222 без остатка на 22, и так далее. Но существует девять четырехзначных чисел, которые имеют 3 единицы:
1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111
Будем считать, что M(n, d) показывает максимальное количество повторений цифры в n-значном простом числе, где d - повторяющаяся цифра, N(n, d) указывает на количество таких простых чисел, а S(n, d) равно сумме всех таких простых чисел.
Таким образом, M(4, 1) = 3 является максимальным числом повторения цифр четырехзначного простого числа, сама повторяющаяся цифра является единицей, и существует N(4, 1) = 9 таких простых чисел, сумма которых равна S(4, 1) = 22275. Оказывается, что для цифры d = 0 можно получить повторение этой цифры всего два раза, однако количество таких простых чисел равно N(4, 0) = 13
Аналогичным способом получим следующие результаты для четырехзначных простых чисел.



Цифра, d
M(4, d)
N(4, d)
S(4, d)


0
2
13
67061


1
3
9
22275


2
3
1
2221


3
3
12
46214


4
3
2
8888


5
3
1
5557


6
3
1
6661


7
3
9
57863


8
3
1
8887


9
3
7
48073



При значениях d от 0 до 9, сумма всех S(4, d) равна 273700.
Найдите сумму всех S(10, d).
 Оригинал
'''