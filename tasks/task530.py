'''
Задача 530
НОД делителей

Каждый делитель d числа n имеет комплиментарный делитель n/d.
Пусть f(n) будет суммой наибольших общих делителей чисел d и n/d из всех положительных делителей d числа n таких, что
$f(n)=\displaystyle\sum\limits_{d|n}\, \text{gcd}(d,\frac n d)$.
Пусть F будет сумматорной функцией от f, такой что
$F(k)=\displaystyle\sum\limits_{n=1}^k \, f(n)$.
Известно, что F(10)=32 и F(1000)=12776.
Найдите F(1015).
 Оригинал
'''