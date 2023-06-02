'''
Задача 795
Чередующаяся сумма НОД


Для положительного целого числа $n$ функция $g(n)$ определена как

$$\displaystyle g(n)=\sum_{i=1}^{n} (-1)^i \gcd \left(n,i^2\right)$$

Например, $g(4) = -\gcd \left(4,1^2\right) + \gcd \left(4,2^2\right) - \gcd \left(4,3^2\right) + \gcd \left(4,4^2\right) = -1+4-1+4=6$.
Также известно, что $g(1234)=1233$.


Пусть $\displaystyle G(N) = \sum_{n=1}^N g(n)$. Известно, что $G(1234) = 2194708$.


Найдите $G(12345678)$.

 Оригинал
'''