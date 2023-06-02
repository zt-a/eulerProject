'''
Задача 771
Псевдогеометрические последовательности


Определим псевдогеометрическую последовательность как конечную последовательность положительных целых чисел $a_0, a_1, \dotsc, a_n$, отвечающую следующим условиям:

$n \geq 4$, т.е. последовательность содержит не менее 5 элементов.
$0 < a_0 < a_1 < \dotsc < a_n$, т.е. последовательность строго возрастающая.
$| a_i^2 - a_{i - 1}a_{i + 1} | \le 2$ для $1 \le i \le n-1$.


Пусть $G(N)$ будет количеством различных псевдогеометрических последовательностей, чьи элементы не превышают $N$.
Например, $G(6) = 4$, так как следующие $4$ последовательности составляют исчерпывающий список:
$1, 2, 3, 4, 5 \qquad 1, 2, 3, 4, 6 \qquad 2, 3, 4, 5, 6 \qquad 1, 2, 3, 4, 5, 6$ 

Также известно, что $G(10) = 26$, $G(100) = 4710$ и $G(1000) = 496805$.

Найдите $G(10^{18})$. В качестве ответа приведите остаток от деления полученного результата на $1\,000\,000\,007$.
 Оригинал
'''