'''
Задача 395
Дерево Пифагора


Дерево Пифагора - это фрактал, сгенерированный следующим образом:


Начните с единичного квадрата. Затем, выбрав одну из его сторон, как основание (в анимации нижняя сторона является основанием):


 Постройте прямоугольный треугольник на противоположной основанию стороне с гипотенузой, совпадающей с этой стороной, и отношением сторон 3:4:5. Заметьте, что меньший катет должен быть справа относительно основания (см. анимацию).
 На каждом катете прямоугольного треугольника постройте квадрат со стороной, совпадающей с этим катетом.
 Повторите это процедуру для обоих квадратов, считая за основания их стороны, касающиеся треугольника.


Фигура, получившаяся после бесконечного числа итераций, является деревом Пифагора.



Можно показать, что существует хотя бы один прямоугольник, чьи стороны параллельны сторонам наибольшего квадрата в дереве Пифагора, и который заключает в себе все дерево Пифагора полностью.


Найдите наименьшую возможную площадь такого прямоугольника и дайте ваш ответ округленным до 10 знака после десятичной точки.


Оригинал
'''