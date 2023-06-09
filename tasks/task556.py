'''
Задача 556
Бесквадратные гауссовы целые

Гауссово целое - это число z = a + bi, где a, b - целые, и i2 = -1.
Гауссовы целые являются подмножеством комплексных чисел, а целые числа являются подмножеством гауссовых целых, для которых b = 0.
Гауссова целая единица - это число, для которого a2 + b2 = 1, т.е. одно из чисел 1, i, -1, -i.
Определим собственное гауссово целое как то, для которого a > 0 и b ≥ 0.
Гауссово целое z1 = a1 + b1i считается делящимся на z2 = a2 + b2i, если z3 = a3 + b3i = z1/z2 является гауссовым целым.
$\frac {z_1} {z_2} = \frac {a_1 + b_1 i} {a_2 + b_2 i} = \frac {(a_1 + b_1 i)(a_2 - b_2 i)} {(a_2 + b_2 i)(a_2 - b_2 i)} = \frac {a_1 a_2 + b_1 b_2} {a_2^2 + b_2^2} + \frac {a_2 b_1 - a_1 b_2} {a_2^2 + b_2^2}i = a_3 + b_3 i$
Итак, z1 делится на z2, если $\frac {a_1 a_2 + b_1 b_2} {a_2^2 + b_2^2}$ и $\frac {a_2 b_1 - a_1 b_2} {a_2^2 + b_2^2}$ - целые.
Например, число 2 делится на 1 + i, потому что число 2/(1 + i) = 1 - i является гауссовым целым.
Гауссово простое число - это гауссово целое, которое делится только на единицу, себя и произведение себя и единицы.
Например, число 1 + 2i - это гауссово простое число, потому что оно делится только на 1, i, -1, -i, 1 + 2i, i(1 + 2i) = i - 2, -(1 + 2i) = -1 - 2i и -i(1 + 2i) = 2 - i.
В то же время, число 2 не является гауссовым простым числом, так как оно делится на 1 + i.
Гауссово целое может быть единственным образом разложено на произведение единицы и гауссовых собственных простых чисел.
Например, 2 = -i(1 + i)2 и 1 + 3i = (1 + i)(2 + i).
Гауссово целое называется бесквадратным, если его разложение на простые множители не содержит повторяющихся гауссовых собственных простых чисел.
Таким образом, число 2 не является бесквадратным гауссовым целым, в то время как число 1 + 3i таковым является.
Единицы и гауссовы простые числа являются бесквадратными по определению.
Пусть f(n) будет количеством собственных бесквадратных гауссовых целых с a2 + b2 ≤ n.
Например, f(10) = 7, потому что числа 1, 1 + i, 1 + 2i, 1 + 3i = (1 + i)(2 + i), 2 + i, 3 и 3 + i = -i(1 + i)(1 + 2i) - бесквадратные, в то время как числа 2 = -i(1 + i)2 и 2 + 2i = -i(1 + i)3 - нет.
Известно, что f(102) = 54, f(104) = 5218 и f(108) = 52126906.
Найдите f(1014).
 Оригинал
'''