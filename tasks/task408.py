'''
Задача 408
Допустимые пути через сетку

Назовем точку (x, y) на единичной сетке недопустимой, если x, y и x + y являются положительными идеальными квадратами.
Например, (9, 16) недопустима, в то время как (0, 4), (3, 1) и (9, 4) - допустимы.
Рассмотрим путь из точки (x1, y1) в точку (x2, y2), состоящий только из единичных шагов в направлении на север или на восток.
Назовем такой путь допустимым, если ни одна из промежуточных точек пути не является недопустимой.
Пусть P(n) будет количеством допустимых путей от (0, 0) до (n, n).
Может быть показано, что P(5) = 252, P(16) = 596994440 и P(1000) mod 1 000 000 007 = 341920854.
Найдите P(10 000 000) mod 1 000 000 007.
 Оригинал
'''