'''
Задача 472
Комфортное расстояние 2

N сидений расположено в ряд. N человек приходят один за другим и занимают места в соответствии со следующими правилами:


Никто не садится рядом с кем-то другим.
Первый человек выбирает любое сидение.
Каждый следующий человек выбирает дальнейшее сидение от всех уже сидящих, в то же время не нарушая правило номер 1. Если есть несколько возможностей, удовлетворяющих этому условию, человек выбирает сидение, расположенное левее всего.

Заметим, что из-за первого правила обязательно останутся незанятые сиденья, а максимальное число рассевшихся человек будет меньше N (для N > 1).
Вот несколько возможных размещений сидящих для N = 15:

Мы видим, что в зависимости от выбора первого человека 15 сидений могут разместить до 7 человек.
Также мы видим, что у первого человека есть 9 возможностей привести число рассаженных людей к максимальному значению.
Пусть f(N) будет количеством выбранных первым человеком сидений, которые приведут к максимальному количеству сидящих людей в ряду из N сидений. Таким образом, f(1) = 1, f(15) = 9, f(20) = 6 и f(500) = 16.
Также, ∑f(N) = 83 для 1 ≤ N ≤ 20 и ∑f(N) = 13343 для 1 ≤ N ≤ 500.
Найдите ∑f(N) для 1 ≤ N ≤ 1012. В качестве ответа приведите последние 8 цифр полученного числа.
 Оригинал
'''