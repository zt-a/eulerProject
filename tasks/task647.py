'''
Задача 647
Линейные преобразования многоугольных чисел


Возможно найти такие натуральные числа $A$ и $B$, что для любого треугольного числа $T_n$ сумма $AT_n +B$ всегда будет треугольным числом. Определим $F_3(N)$ как сумму $(A+B)$ для всех возможных пар $(A,B)$ при $\max(A,B)\le N$. Например, $F_3(100) = 184$.


Многоугольные числа являются обобщением треугольных чисел. Назовем многоугольные числа с параметром $k$ $k$-угольными числами. Формулой для $n$-того $k$-угольного числа является $\frac 12n\big(n(k-2)+4-k\big)$, где$n \ge 1$. Например, при $k = 3$ получим $\frac 12n(n+1)$ - формулу треугольных чисел.


Утверждение выше верно для пятиугольных, семиугольных и, по сути, любых $k$-угольных чисел с нечетным $k$. Например, при $k=5$ имеем пятиугольные числа и можем найти такие натуральные числа $A$ и $B$, что для любого пятиугольного числа $P_n$ сумма $AP_n+B$ всегда будет пятиугольным числом. Определим $F_5(N)$ как сумму $(A+B)$ для всех таких возможных пар $(A,B)$ при $\max(A,B)\le N$.


Похожим образом определим $F_k(N)$ для нечетного $k$. Известно, что $\sum_{k} F_k(10^3) = 14993$, где сумма взята для всех нечетных $k = 3,5,7,\ldots$.


Найдите $\sum_{k} F_k(10^{12})$, где сумма взята для всех нечетных $k = 3,5,7,\ldots$

 Оригинал
'''