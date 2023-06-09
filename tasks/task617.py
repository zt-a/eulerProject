'''
Задача 617
Последовательность зеркальных степеней

Для двух целых чисел $n,e > 1$ определим $(n,e)$-ПЗС (последовательность зеркальных степеней) как бесконечную последовательность целых чисел $(a_i)_{i\ge 0}$, такую что для всех $i\ge 0$, $a_{i+1} = min(a_i^e,n-a_i^e)$ и $a_i > 1$.

Примерами таких последовательностей являются две $(18,2)$-ПЗС последовательности, созданные чередованием чисел $2$ и $4$.
Заметим: несмотря на то, что последовательность уникально определяется $n,e$ и $a_0$, для большинства их значений такой последовательности не существует. Например, не существует $(n,e)$-ПЗС последовательности для $n < 6$.
Определим $C(n)$ как количество $(n,e)$-ПЗС для какого-либо $e$ и $\displaystyle D(N) = \sum_{n=2}^N {C(n)}$.

Известно, что $D(10) = 2$, $D(100) = 21$, $D(1000) = 69$, $D(10^6) = 1303$ и $D(10^{12}) = 1014800$.
Найдите $D(10^{18})$.
 Оригинал
'''