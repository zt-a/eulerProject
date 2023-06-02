'''
Задача 364
Комфортное расстояние


N сидений расположено в ряд. N человек приходят один за другим и занимают места в соответствии со следующими правилами:


Если есть место, прилежащие к которому сидения свободны - занять это место.
Если таковые отсутствуют, но есть место с только одним занятым прилежащим сидением - занять это место..
Во всех остальных случаях занять одно из оставшихся свободных мест. 


Пусть T(N) будет количеством возможностей для N человек занять N сидений следуя данным правилам.

Нижеприведенное изображение показывает T(4)=8.





Можно убедиться, что T(10) = 61632 и T(1 000) mod 100 000 007 = 47255094.


Найдите T(1 000 000) mod 100 000 007.

 Оригинал
'''