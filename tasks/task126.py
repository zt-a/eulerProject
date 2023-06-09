'''
Задача 126
Слои параллелепипеда

Минимальное количество единичных кубов, необходимое для покрытия всех видимых граней прямоугольного параллелепипеда размерами 3 x 2 x 1, составляет двадцать два.



Если мы добавим второй слой кубов на полученное тело, то потребуется еще сорок шесть кубов для покрытия каждой видимой грани. Для третьего слоя понадобится еще семьдесят восемь кубов, а для четвертого – сто восемнадцать кубов, покрывающих каждую грань тела.
Однако, для покрытия граней прямоугольного параллелепипеда размерами 5 x 1 x 1 первым слоем, требуются те же двадцать два куба; похожим образом, для первого слоя каждого из прямоугольных параллелепипедов размерами 5 x 3 x 1, 7 x 2 x 1, и 11 x 1 x 1 требуется сорок шесть кубов.
Определим C(n) как число прямоугольных параллелепипедов, содержащих n кубов в одном из своих слоев. Таким образом, C(22) = 2, C(46) = 4, C(78) = 5, и C(118) = 8.
Оказывается, что 154 – наименьшее значение n, при котором C(n) = 10.
Найдите наименьшее значение n, при котором C(n) = 1000.

Оригинал
'''