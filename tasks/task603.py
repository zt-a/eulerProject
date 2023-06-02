'''
Задача 603
Суммы подстрок соединений простых чисел

Пусть $S(n)$ будет суммой всех смежных подстрок целых чисел, которые могут быть образованы из целого числа $n$. Подстроки не должны обязательно быть различными.
Например, $S(2024) = 2 + 0 + 2 + 4 + 20 + 02 + 24 + 202 + 024 + 2024 = 2304$.
Пусть $P(n)$ будет целым числом, образованным соединением первых $n$ простых чисел. Например, $P(7) = 2357111317$.
Пусть $C(n, k)$ будет целым числом, образованным соединением $k$ копий $P(n)$. Например, $C(7, 3) = 235711131723571113172357111317$.
Рассчитайте $S(C(10^6, 10^{12}))$ mod $(10^9 + 7)$.
 Оригинал
'''