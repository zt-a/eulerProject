'''
Задача 644
Квадраты на прямой

Сэм и Том испытывают игру, состоящую в (частичном) покрытии данного отрезка длины $L$, по очереди располагая на нем единичные квадраты. 
Как показано ниже, квадрат можно расположить одним из двух способов: или "прямо", поместив на отрезке середины двух противоположных сторон квадрата, или "диагонально", поместив на отрезке противоположные вершины квадрата. Размещенный таким образом квадрат может касаться других квадратов, но не может перекрывать ни один из ранее помещенных квадратов.
Игрок, поместивший последний единичный квадрат на отрезок, побеждает.


Если Сэм всегда ходит первым, игроки быстро выяснили, что он может запросто выигрывать каждый раз, помещая первый квадрат в середину отрезка, что сделало игру скучной. 

Поэтому они решили сделать первый ход Сэма случайным, подкидывая честную монету для определения, будет ли первый квадрат помещен прямо или диагонально, а также случайно выбирая положение первого квадрата на отрезке, причем все возможные расположения имеют одинаковую вероятность. Выигрыш Сэма от каждой игры считается равным 0, если он ее проигрывает, и $L$, если выигрывает. Предполагая, что оба игрока играют оптимальным образом после первого хода Сэма, можно заметить, что ожидаемый выигрыщ Сэма $e(L)$ зависит только от длины отрезка.

Например, если $L=2$, Сэм победит с вероятностью 1, поэтому $e(2)= 2$. 
При $L=4$ вероятность победы будет равна 0.33333333 для прямого расположения и 0.22654092 для диагонального, что приведет к $e(4)=1.11974851$ (округленному до 8 знака после десятичной точки). 

Будучи заинтересованными в оптимальном для Сэма значении $L$, определим $f(a,b)$ как максимальное значение $e(L)$ при выбраннном $L \in [a,b]$. 
Известно, что $f(2,10)=2.61969775$ достигается при $L= 7.82842712$, и $f(10,20)=
5.99374121$ (оба округлены до 8 знака).

Найдите $f(200,500)$, округленное до 8 знака после десятичной точки.

'''