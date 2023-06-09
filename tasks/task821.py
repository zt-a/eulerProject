'''
Задача 821
123-разделимые


Множество целых чисел $S$ называется 123-разделимым, если множества $S$, $2S$ и $3S$ являются непересекающимися. Множества $2S$ и $3S$ получены умножением всех элементов множества $S$ на $2$ и $3$ соответственно.

Определим $F(n)$ как максимальное количество элементов $$(S\cup 2S \cup 3S)\cap \{1,2,3,\ldots,n\}$$,
где $S$ охватывает все 123-разделимые множества.

Например, $F(6) = 5$ можно достичь или при $S = \{1,4,5\}$, или при $S = \{1,5,6\}$.
Также известно, что $F(20) = 19$.

Найдите $F(10^{16})$.
 Оригинал
'''