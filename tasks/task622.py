'''
Задача 622
Перетасовка колоды


Перетасовка колоды выполняется следующим образом: колода карт разделяется на две равные половины, верхняя половина берется в левую руку, а нижняя - в правую. Далее, карты идеально чередуются: верхняя карта правой половины вставляется сразу после верхней карты левой половины, вторая карта правой половины - сразу после второй карты левой, и так далее. (Заметим, что этот процесс сохраняет положение верхней и нижней карты колоды).


Пусть $s(n)$ будет минимальным количеством последовательных перетасовок, необходимых, чтобы вернуть колоду из $n$ кард в изначальный порядок, где $n$ - положительное четное число.

Удивительно, но стандартная колода из $52$ карт вернется к изначальному порядку карт всего после $8$ идеальных перетасовок, поэтому $s(52) = 8$. Можно показать, что колода из $86$ карт тоже вернется к своему изначальному порядку после ровно $8$ перетасовок, и сумма всех значений $n$, удовлетворяющих $s(n) = 8$, равна $412$.


Найдите сумму всех значений $n$, удовлетворяющих $s(n) = 60$.

 Оригинал
'''