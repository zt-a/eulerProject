'''
Задача 308
Удивительный автомат для генерации простых чисел

Программа, написанная на языке программирования Fractran, состоит из списка дробей.
Внутреннее состояние виртуальной машины Fractran — это натуральное число, которое изначально устанавливается равным начальному числу генератора (seed value). При каждой итерации Fractran-программы число состояния машины умножается на первую дробь в списке, которая даст в результате целое число.
Например, одна из программ на Fractran, написанная Джоном Хортоном Конвейем для генерации простых чисел, состоит из следующих 14 дробей:



1791

,

7885

,

1951

,

2338

,

2933

,

7729

,

9523

,

7719

,

117

,

1113

,

1311

,

152

,

17

,

551

.


При начальном значении генератора 2, последовательное выполнение итераций программы производит последовательность:
15, 825, 725, 1925, 2275, 425, ..., 68, 4, 30, ..., 136, 8, 60, ..., 544, 32, 240, ...
В этой последовательности появляются следующие степени двойки: 22, 23, 25, ...
Можно показать, что все степени двойки в этой последовательности имеют простые показатели и, кроме того, все простые числа в показателях степеней двойки появляются в правильном порядке.
Если использовать приведенную выше программу на Fractran при решении 7-й задачи проекта «Эйлер» (найдите 10001-е простое число), то сколько итераций потребуется, прежде чем программа выдаст число 210001ое простое число?
 Оригинал
'''