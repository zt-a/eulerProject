'''
Задача 803
Псевдослучайная последовательность

Rand48 - это генератор псевдослучайных чисел, используемый в некоторых языках программирования. Он генерирует последовательность из любого данного целого числа $a_0$, используя правило $a_n = (25214903917 \cdot a_{n - 1} + 11) \bmod 2^{48}$.


Пусть $b_n = \lfloor a_n / 2^{16} \rfloor \bmod 52$.
Последовательность $b_0, b_1, \dots$ переводится в строку $c = c_0c_1\dots$ по следующему правилу:
$0 \rightarrow$ a, $1\rightarrow$ b, $\dots$, $25 \rightarrow$ z, $26 \rightarrow$ A, $27 \rightarrow$ B, $\dots$, $51 \rightarrow$ Z.


Например, если мы выберем $a_0 = 123456$, то строка $c$ будет начинаться так: "bQYicNGCY$\dots$".
Более того, начиная с индекса $100$, мы впервые встретим подстроку "RxqLBfWzv".


С другой стороны, если $c$ начинается с "EULERcats$\dots$", то $a_0$ должно быть равно $78580612777175$.


Теперь предположим, что строка $c$ начинается с "PuzzleOne$\dots$".
Найдите начальный индекс первого появления подстроки "LuckyText" в $c$.

 Оригинал
'''