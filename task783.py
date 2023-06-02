'''
Задача 783
Вазы


При заданных положительных целых числах $n$ и $k$ начнем с вазы, которая содержит $kn$ белых шариков. Затем мы выполняем $n$ ходов, на каждом из которых добавляем в вазу $k$ черных шариков и затем вынимаем из нее $2k$ случайных шариков.

Пусть $B_t(n,k)$ будет количеством черных шариков, извлеченных на ходе $t$.

Далее определим $E(n,k)$ как математическое ожидание $\displaystyle \sum_{t=1}^n B_t(n,k)^2$.

Известно, что $E(2,2) = 9.6$

Найдите $E(10^6,10)$. Округлите ваш ответ до ближайшего целого числа.
 Оригинал
'''