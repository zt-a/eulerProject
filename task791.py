'''
Задача 791
Среднее и дисперсия

Определим среднее значение $k$ чисел $x_1, ..., x_k$ как $\bar{x} = \frac{1}{k} \sum_i x_i$. Дисперсия этих чисел определяется как $\frac{1}{k} \sum_i \left( x_i - \bar{x} \right) ^ 2$.
Пусть $S(n)$ будет суммой всех четверок целых чисел $(a,b,c,d)$, удовлетворяющих $1 \leq a \leq b \leq c \leq d \leq n$ таких, что их среднее значение ровно в два раза больше их дисперсии.
Для $n = 5$ существует $5$ таких четверок, а именно: $(1, 1, 1, 3), (1, 1, 3, 3), (1, 2, 3, 4), (1, 3, 4, 4), (2, 2, 3, 5)$.
Отсюда $S(5)=48$. Также известно, что $S(10^3)=37048340$.
Найдите $S(10^8)$. В качестве ответа приведите остаток от деления полученного результата на $433494437$.
 Оригинал
'''