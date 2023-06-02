'''
Задача 502
Счет замков

Определим блок как прямоугольник с высотой 1 и целочисленной длиной. Назовем конструкцию из сложенных друг на друге блоков замком.
Дана игровая сетка шириной w единиц и высотой h единиц, в которой генерируется замок в соответствии со следующими правилами:

Блоки могут располагаться на других блоках, если они не вылезают за края и не нависают над пустым пространством.
Все блоки выровнены строго по сетке.
Любые два соседних блока в одном ряду должны быть отделены хотя бы одной единицей пустого пространства.
Нижний ряд занят блоком длиной w.
Высота замка в его самой высокой точке равна h.
Замок составлен из четного количества блоков.

Ниже приведен пример замка для w = 8 и h = 5:

Пусть F(w,h) будет количеством возможных следующих правилам замков при параметрах сетки w и h.
Например, F(4,2) = 10, F(13,10) = 3729050610636, F(10,13) = 37959702514 и F(100,100) mod 1 000 000 007 = 841913936.
Найдите F(1012,100) + F(10000,10000) + F(100,1012) mod 1 000 000 007.
 Оригинал
'''