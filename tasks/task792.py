'''
Задача 792
Слишком много двоек


Определим $\nu_2(n)$ как наибольшее целое число $r$, такое что $2^r$ делит $n$ нацело. Например, $\nu_2(24) = 3$.


Определим $\displaystyle S(n)  = \sum_{k = 1}^n (-2)^k\binom{2k}k$ и $u(n) = \nu_2\Big(3S(n)+4\Big)$.


Например, если $n = 4$, то $S(4) = 980$ и $3S(4) + 4 = 2944 = 2^7 \cdot 23$, отсюда $u(4) = 7$.
Вам также известно, что $u(20) = 24$.


Также определим $\displaystyle U(N) = \sum_{n = 1}^N u(n^3)$. Известно, что $U(5) = 241$.


Найдите $U(10^4)$.

 Оригинал
'''