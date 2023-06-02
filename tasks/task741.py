'''
Задача 741
Раскрашивание двоичной сетки


Пусть $f(n)$ будет количеством способов, как можно раскрасить каждую ячейку квадратной сетки $n\times n$ в белый или черный цвет, так чтобы каждый ряд и столбец содержали ровно две черные ячейки.
Например, $f(4)=90$, $f(7) = 3110940$ и $f(8) = 187530840$.


Пусть $g(n)$ будет количеством способов раскраски в $f(n)$, которые уникальны с точностью до зеркальных отражений и поворотов.
Известно, что $g(4)=20$, $g(7) = 390816$ и $g(8) = 23462347$. Значит, $g(7)+g(8) = 23853163$.


Найдите $g(7^7) + g(8^8)$. В качестве ответа приведите остаток от деления полученного результата на $1\,000\,000\,007$.

 Оригинал
'''