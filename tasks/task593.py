'''
Задача 593
Мимолетные медианы

Определим две последовательности $S = \{S(1), S(2), ..., S(n)\}$ и $S_2 = \{S_2(1), S_2(2), ..., S_2(n)\}$:
$S(k) = (p_k)^k$ mod $10007$, где $p_k$ - $k$-тое простое число.
$S_2(k) = S(k) + S(\lfloor\frac{k}{10000}\rfloor + 1)$, где $\lfloor \cdot \rfloor$ обозначает функцию пол.
Тогда пусть $M(i, j)$ будет медианой элементов от $S_2(i)$ до $S_2(j)$ включительно. Например, $M(1, 10) = 2021.5$ и $M(10^2, 10^3) = 4715.0$.
Пусть $F(n, k) = \sum_{i=1}^{n-k+1} M(i, i + k - 1)$. Например, $F(100, 10) = 463628.5$ и $F(10^5, 10^4) = 675348207.5$.
Найдите $F(10^7, 10^5)$. Если сумма не является целой, используйте $.5$ для обозначения половины. В противном случае используйте $.0$.
 Оригинал
'''