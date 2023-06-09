'''
Задача 753
Уравнение Ферма

Последняя теорема Ферма гласит, что не существует трех натуральных чисел $a$, $b$, $c$, удовлетворяющих уравнению
$$a^n+b^n=c^n$$
для любого целого значения $n$ больше 2.
В рамках этой задачи рассмотрим только случай $n=3$. Для определенных значений $p$ возможно решить конгруэнцию:
$$a^3+b^3 \equiv c^3 \pmod{p}$$
Для простого числа $p$ определим $F(p)$ как количество целочисленных решений этой конгруэнции для $1 \le a,b,c < p$.
Известно, что $F(5) = 12$ и $F(7) = 0$.
Найдите сумму $F(p)$ по всем простым числам $p$ меньше $6\,000\,000$.
 Оригинал
'''