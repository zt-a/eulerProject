'''
Задача 693
Генератор конечных последовательностей

Два натуральных числа $x$ и $y$ ($x > y$) могут быть использованиы, чтобы сгенерировать последовательность следующим образом:

Первый элемент $a_x = y$,
$a_{z+1} = a_z^2 \bmod z$ для $z = x, x+1,x+2,\ldots$ и
генерирование заканчивается на элементе, равном 0 или 1.

Число элементов этой последовательности обозначается $l(x,y)$.
Например, при $x = 5$ и $y = 3$ мы получим $a_5 = 3$, $a_6 = 3^2 \bmod 5 = 4$, $a_7 = 4^2\bmod 6 = 4$ и т.д. Это даст последовательность из 29 элементов:
$3,4,4,2,4,7,9,4,4,3,9,6,4,16,4,16,16,4,16,3,9,6,10,19,25,16,16,8,0$
Поэтому $l(5,3) = 29$.
Определим $g(x)$ как максимальное значение $l(x,y)$ для $y < x$. Например, $g(5) = 29$.
Далее, определим $f(n)$ как максимальное значение $g(x)$ для $x \le n$. Например, $f(100) = 145$ и $f(10\,000) = 8824$.
Найдите $f(3\,000\,000)$.
 Оригинал
'''