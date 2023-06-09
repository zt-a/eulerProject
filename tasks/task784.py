'''
Задача 784
Обратные пары


Назовем пару положительных целых чисел $p$, $q$ ($p \lt q$) обратной, если существует положительное целое число $r\lt p$, такое что $r$ равно как обратному остатку от деления $p$ на $q$, так и обратному остатку от деления $q$ на $p$.

Например, $(3,5)$ - обратная пара для $r=2$.
Пусть $F(N)$ будет общей суммой $p+q$ для всех обратных пар $(p,q)$, где $p \le N$.

$F(5)=59$ ввиду следующих четырех обратных пар: $(3,5)$, $(4,11)$, $(5,7)$ и $(5,19)$.
Также известно, что $F(10^2) = 697317$.

Найдите $F(2\cdot 10^6)$.
 Оригинал
'''