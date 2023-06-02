'''
Задача 289
Циклы Эйлера

Пусть C(x,y) - окружность, проходящая через точки
(x, y), (x, 
y+1), (x+1, y) и (x+1,
 y+1).
Предположим, что для натуральных значений m и n, E(m,n) является структурой из m·n окружностей:
 { C(x,y): 0 ≤ x
 < m, 0 ≤ y 
< n, x и y являются целыми числами }
Цикл Эйлера в E(m,n) - замкнутая траектория, проходящая через каждую из дуг только один раз.
Существует множество таких траекторий для E(m,n), однако нас интересуют только те, которые не являются самопересекающимися:
такая траектория проходит через все узлы сетки, но никогда не пересекается с самой собой.
На рисунке ниже показана структура E(3,3), а также пример цикла Эйлера без самопересечений.

Пусть L(m,n) - число циклов Эйлера без пересечений в пределах структуры E(m,n).
К примеру, L(1,2) = 2, L(2,2) = 37 и L(3,3) = 104290.
Найдите L(6,10) mod 1010.
 Оригинал
'''