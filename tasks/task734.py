'''
Задача 734
Бит простого числа


Логическое ИЛИ от двух битов равно 0, если оба бита равны 0, в противном случае оно равно 1.
Побитное ИЛИ от двух натуральных чисел выполняет операцию логического ИЛИ над каждой парой соответствующих битов в двоичном представлении вводных чисел.


Например, побитное ИЛИ от $10$ и $6$ равно $14$, так как $10 = 1010_2$, $6 = 0110_2$ и $14 = 1110_2$.


Пусть $T(n, k)$ будет количеством кортежей длиной $k$ $(x_1, x_2,\cdots,x_k)$ таких что


каждое $x_i$ является простым числом $\leq n$
побитное ИЛИ от кортежа является простым числом $\leq n$


Например, $T(5, 2)=5$. Первые пять кортежей длиной 2: (2, 2), (2, 3), (3, 2), (3, 3) и (5, 5).

Известно, что $T(100, 3) = 3355$ и $T(1000, 10) \equiv 2071632 \pmod{1\,000\,000\,007}$


Найдите $T(10^6,999983)$. В качестве ответа приведите остаток от деления полученного результата на $1\,000\,000\,007$

 Оригинал
'''