'''
Задача 300
Сворачивание белка

Очень упрощая, можно считать белки цепочками, состоящими из гидрофобных (H) и полярных (P) элементов, например: HHPPHHHPHHPH. 
В этой задаче важна ориентация белка: к примеру, цепочка HPP считается отличной от PPH. Таким образом, существует 2n различных белков, состоящих из n элементов.
Если наблюдать эти цепочки в природе, то они всегда свернуты таким образом, чтобы количество точек соприкосновения H-H было по возможности больше, т. к. это энергетически выгодно.
В результате H-элементы стремятся собраться во внутренней части, а P-элементы - снаружи.
Разумеется, настоящие белки свернуты в трех измерениях, но мы будем рассматривать только сворачивание белков в двух измерениях.
Рисунок ниже показывает два возможных способа сворачивания белка из нашего примера (места соприкосновения H-H показаны красными точками).

Результат сворачивания, показанный слева, имеет только 6 точек соприкосновения H-H, поэтому никогда не получился бы естественным образом.
С другой стороны, конформация справа имеет 9 точек соприкосновения H-H, что является оптимальным для этой цепочки.
Если принять вероятности нахождения элементов H и P равными в любом месте цепочки, то выясняется, что среднее количество точек соприкосновения H-H в оптимальной конформации случайной белковой цепочки длиной 8 равна 850 / 28=3.3203125.
Каково среднее количество точек соприкосновения H-H в оптимальной конформации случайной белковой цепочки длиной 15?
Дайте ответ, используя столько десятичных знаков, сколько необходимо для точного результата.
 Оригинал
'''