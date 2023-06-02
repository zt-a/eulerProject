'''
Задача 820
$N$-я цифра обратных чисел

Пусть $d_n(x)$ будет $n$-ой десятичной цифрой дробной части числа $x$ или равно $0$, если дробная часть числа имеет содержит $n$ цифр.
Например:

$d_7 \mathopen{}\left( 1 \right)\mathclose{} = d_7 \mathopen{}\left( \frac 1 2 \right)\mathclose{} = d_7 \mathopen{}\left( \frac 1 4 \right)\mathclose{} = d_7 \mathopen{}\left( \frac 1 5 \right)\mathclose{} = 0$
$d_7 \mathopen{}\left( \frac 1 3 \right)\mathclose{} = 3$, так как $\frac 1 3 =$ 0.3333333333...
$d_7 \mathopen{}\left( \frac 1 6 \right)\mathclose{} = 6$, так как $\frac 1 6 =$ 0.1666666666...
$d_7 \mathopen{}\left( \frac 1 7 \right)\mathclose{} = 1$, так как $\frac 1 7 =$ 0.1428571428...

Пусть $\displaystyle  S(n) = \sum_{k=1}^n d_n \mathopen{}\left( \frac 1 k \right)\mathclose{}$.
Известно, что:

$S(7) = 0 + 0 + 3 + 0 + 0 + 6 + 1 = 10$
$S(100) = 418$

Найдите $S(10^7)$.
 Оригинал
'''