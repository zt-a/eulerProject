'''
Задача 503
Уступить или настоять

Алиса играет в игру с n картами, пронумерованными от 1 до n.
Игра состоит из повторения следующих трех шагов:
(1) Алиса берет случайную карту.
(2) Алиса не видит, какое на этой карте число. Вместо этого Боб - один из ее друзей - видит число и говорит Алисе, сколько увиденных до этого чисел было больше этого числа.
(3) Алиса может завершить или продолжить игру. Если она решает закончить, количество ее очков становится равно последнему открытому числу. Если она решает продолжить, эта карта убирается из игры и Алиса снова начинает с шага (1). Если больше не осталось никаких карт, Алиса вынуждена закончить игру этим ходом.
Пусть F(n) будет ожидаемым количеством очков Алисы, если она выберет оптимальную стратегию для получения наименьшего количества очков.
Например, F(3) = 5/3. В первой итерации ей стоит продолжить игру. Во второй итерации ей стоит прекратить игру, если Боб скажет, что одно ранее увиденное число было больше того, которое он видит сейчас. В противном случае, ей стоит продолжить игру.
Можно также показать, что F(4) = 15/8 и F(10) ≈ 2.5579365079.
Найдите F(106). Дайте ответ округленным до 10 цифр после десятичной точки.
 Оригинал
'''