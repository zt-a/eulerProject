'''
Задача 124
Упорядоченные радикалы

Радикалом числа n, rad(n), является произведение уникальных простых множителей числа n. К примеру, 504 = 23 × 32 × 7, таким образом, rad(504) = 2 × 3 × 7 = 42.
Если подсчитать rad(n) для 1 ≤ n ≤ 10 и упорядочить их по rad(n), а затем по n для одинаковых значений радикалов, получим

Неупорядоченная функция
 
Упорядоченная функция
n
rad(n)
 
n
rad(n)
k
11
 
111
22
 
222
33
 
423
42
 
824
55
 
335
66
 
936
77
 
557
82
 
668
93
 
779
1010
 
101010

Пусть E(k) будет k-м элементом в упорядоченной колонне n; к примеру, E(4) = 8, а E(6) = 9.
Найдите E(10000), если функция rad(n) упорядочена для 1 ≤ n ≤ 100000.

Оригинал
'''