'''
Задача 376
Нетранзитивные наборы кубиков


Рассмотрим следующий набор кубиков с нестандартно размеченными гранями:


Кубик A: 1 4 4 4 4 4
Кубик B: 2 2 2 5 5 5
Кубик C: 3 3 3 3 3 6


Два игрока играют в игру, по очереди выбирая кубик и кидая его. Игрок, выкинувший наибольшее число, побеждает.


Если первый игрок берет кубик A, а второй игрок выбирает B, мы получаем

P(второй игрок победит) = 7/12 > 1/2


Если первый игрок берет кубик B, а второй игрок выбирает C, мы получаем

P(второй игрок победит) = 7/12 > 1/2


Если первый игрок берет кубик C, а второй игрок выбирает A, мы получаем

P(второй игрок победит) = 25/36 > 1/2


Итак, какой бы кубик первый игрок ни выбрал, второй игрок может выбрать другой кубик и получить более, чем 50% вероятность победить.

Набор кубиков, имеющий такое свойство, называется нетранзитивным набором кубиков.


Мы хотим исследовать, сколько существует нетранзитивных наборов кубиков. Предположим следующие условия:


Всего есть три шестигранных кубика, каждая грань которых имеет от 1 до N точек включительно.
Кубики с одинаковым набором точек на всех гранях идентичны независимо от их расположения.
Одно и то же количество точек может присутствовать на гранях разных кубиков. Если оба игрока выкидывают одинаковое число, никто не побеждает.
Наборы кубиков {A,B,C}, {B,C,A} и {C,A,B} - это один и тот же набор.


Для N = 7 мы нашли, что существует 9780 таких наборов.
Сколько существует нетранзитивных наборов для N = 30 ?

 Оригинал
'''