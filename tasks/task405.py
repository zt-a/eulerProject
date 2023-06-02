'''
Задача 405
Прямоугольная плитка


Мы хотим выложить плиткой прямоугольник, длина которого в два раза больше ширины.
Пусть T(0) будет выкладкой, состоящей из одного прямоугольника.
Для n > 0, пусть T(n) будет получено из T(n-1) путем замещения всех плиток следующим образом:





Нижеприведенная анимация иллюстрирует выкладки T(n) для n от 0 до 5:





Пусть f(n) будет количеством точек, в которых касаются друг друга четыре плитки в выкладке T(n).
Например, f(1) = 0, f(4) = 82 и f(109) mod 177 = 126897180.


Найдите f(10k) для k = 1018, в качестве ответа приведите остаток от деления полученного числа на 177.


Оригинал
'''