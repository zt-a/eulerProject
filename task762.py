'''
Задача 762
Амебы на 2D-сетке

Рассмотрим двухмерную квадратную сетку. Сетка состоит из 4 рядов и бесконечного числа столбцов.
Амеба, находящаяся в квадрате $(x, y)$ может разделиться на две амебы, которые займут квадраты $(x+1,y)$ и $(x+1,(y+1) \bmod 4)$ при условии, что эти квадраты пусты.
Изображения ниже показывают два случая, в которых амеба находится в квадрате A каждой сетки. Когда она делится, вместо нее появляются две амебы на квадратах, обозначенных B:




Изначально на сетке находится только одна амеба в квадрате $(0, 0)$. После $N$ делений на сетке будет расположено $N+1$ амеб. Расположение, которое можно достичь несколькими разными способами, засчитывается только один раз. Пусть $C(N)$ будет количеством различных возможных расположений после $N$ делений.
Например, $C(2) = 2$, $C(10) = 1301$, $C(20)=5895236$ и последние девять цифр $C(100)$ - $125923036$.
Найдите $C(100\,000)$. В качестве ответа приведите последние девять цифр полученного числа.
 Оригинал
'''