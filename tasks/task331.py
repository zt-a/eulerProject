'''
Задача 331
Флип Флоп

На квадратном поле расставлены N×N фишек. У каждой фишки есть белая сторона и черная сторона.
Во время очередного хода происходит выбор фишки, после чего все фишки в соответствующем ряду и колонне переворачиваются: т.е. переворачивается 2×N-1 фишек. Игра завершается, когда все фишки повернуты белой стороной к верху. Ниже представлен пример игры на поле размерами 5×5 клеток.

Можно доказать, что 3 - минимальное число ходов, необходимое для завершения этой игры.
На игровом поле размерами N×N нижняя левая фишка имеет координаты (0,0), нижняя правая фишка - координаты (N-1,0), а верхняя левая - (0,N-1). 
Обозначим через CN следующую конфигурацию игрового поля размерами N×N клеток: Фишка с координатами (x,y), удовлетворяющими неравенство , повернута кверху черной стороной, в противном случае - белой стороной. К примеру, конфигурация C5 показана на рисунке выше.
Пусть T(N) - минимальное число ходов, необходимых для завершения игры с исходной конфигурации поля CN.
Если конфигурация CN не может привести к завершению игры, то T(N)=0. Как было показано, T(5)=3. Кроме того, известно, что T(10)=29 и T(1 000)=395253.
Найдите .
 Оригинал
'''