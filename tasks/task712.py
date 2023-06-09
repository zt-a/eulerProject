'''
Задача 712
Разница экспонент


Для любого целого числа $n>0$ и простого числа $p$ определим $\nu_p(n)$ как наибольшее целое число $r$, такое что $p^r$ делит $n$ нацело. 


Определим $$D(n, m) = \sum_{p \text{ prime}} \left| \nu_p(n) - \nu_p(m)\right|.$$ Например, $D(14,24) = 4$.


Далее, определим $$S(N) = \sum_{1 \le n, m \le N} D(n, m).$$ Известно, что $S(10) = 210$ и $S(10^2) = 37018$.


Найдите $S(10^{12})$. В качестве ответа приведите остаток от деления полученного результата на $1\,000\,000\,007$.

 Оригинал
'''