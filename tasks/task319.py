'''
Задача 319
Ограниченные последовательности


Пусть x1, x2,...,
  xn - последовательность длиной n, для которой справедливо:

x1
 = 2
xi-1
    < xi при всех 1 < i < n
(xi) j < (xj + 1)i
 для всех i и j при 1 ≤ i, j
  ≤
  n


Существует всего пять таких последовательностей длиной 2, а именно:
{2,4}, {2,5}, {2,6}, {2,7} и {2,8}.
Существует 293 такие последовательности длиной 5. Ниже представлены три примера:
{2,5,11,25,55}, {2,6,14,36,88}, {2,8,22,64,181}.


Обозначим через t(n) число таких последовательностей длиной n.
Известно, что t(10) = 86195 и t(20) = 5227991891.


Найдите t(1010)
 и приведите ответ по модулю 109.

 Оригинал
'''