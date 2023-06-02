'''
Задача 183
Максимальное произведение частей

Пусть N - натуральное число, и пусть N можно разбить на k равных частей r = N/k, таких, что N = r + r + ... + r.
Пусть P - произведение этих частей, P = r × r × ... × r = rk.
К примеру, если 11 разбить на пять равных частей, 11 = 2.2 + 2.2 + 2.2 + 2.2 + 2.2, то P = 2.25 = 51.53632.
Пусть M(N) = Pmax при заданном значении N.
Оказывается, что для N = 11 максимум можно найти, разбив число 11 на четыре равные части, что в итоге даст Pmax = (11/4)4, т.е. M(11) = 14641/256 = 57.19140625 - получена непериодическая десятичная дробь.
Однако, при N = 8 максимум можно найти, разбив это число на три равные части, так что M(8) = 512/27. В итоге получена периодическая десятичная дробь.
Пусть D(N) = N, если M(N) является периодической дробью и D(N) = -N, если M(N) является непериодической дробью.
Например, ΣD(N) для 5 ≤ N ≤ 100 равна 2438.
Найдите ΣD(N), если 5 ≤ N ≤ 10000.
 Оригинал
'''