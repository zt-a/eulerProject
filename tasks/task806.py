'''
Задача 806
Ним на ханойской башне

Эта задача совмещают игру ним с ханойской башней. Для краткого введения в правила этих игр обратитесь к задаче 301 и задаче 497 соответственно.
Единственное кратчайшее решение для задачи ханойской башни с $n$ дисками и $3$ столбиками требует $2^n-1$ ходов. Пронумеруем расположения в этом решении индексами от 0 (начальное расположение, все диски на первом столбике) до $2^n-1$ (конечное расположение, все диски на третьем столбике).
Каждое из этих $2^n$ расположений можно считать начальной конфигурацией для игры ним, в которой два игрока по очереди выбирают один из столбиков выбирают один из столбиков и убирают с него любое положительное число дисков. Побеждает игрок, который убрал последний диск.
Определим $f(n)$ как сумму индексов расположений, начиная в которых игру ним, первый игрок проиграет (полагая, что оба игрока придерживаются оптимальной стратегии).
Для $n=4$ индексы проигрышных позиций в кратчайшем решении равны 3, 6, 9 и 12. Итак, $f(4) = 30$.
Известно, что $f(10) = 67518$.
Найдите $f(10^5)$. В качестве ответа приведите остаток от деления полученного результата на $1\,000\,000\,007$.
 Оригинал
'''