'''
Задача 353
Луна с риском


Луну можно описать сферой C(r) с центром в точке с координатами (0,0,0) и радиусом r.


Предположим, что на поверхности луны C(r) расположены две станции с цело-численными координатами. Станцию в точке с координатами (0,0,r) назовем станцией Северного Полюса, а станцию в точке с координатами (0,0,-r) - соответственно, станцией Южного Полюса.


Все станции соединены между собой кратчайшими путями по большим дугам, проходящим через точки расположения станций. Переход от одной станции к другой - рискован. Если d - длина пути между двумя станциями, то (d/(π r))2 - мера риска такого путешествия (назовем ее риском пути). Если путешествие происходит более чем между двумя соседними станциями, то риск всего пути определяется суммой рисков всех использованных путей.


Длина пути путешествия от станции Северного Полюса до станции Южного Полюса составляет πr и его риск равен 1. Путешествие от станции Северного Полюса до станции Южного Полюса по (0,r,0) будет настолько же длинным, однако с меньшим риском: (½πr/(πr))2 +(½πr/(πr))2=0.5.


Наименьший риск пути от станции Северного Полюса до станции Южного Полюса на поверхности C(r) составляет M(r).


Дано, что M(7)=0.1784943998 после округления до 10 знака после десятичной точки.


Найдите ∑M(2n-1) для всех 1≤n≤15.


Ответ округлите до 10 знака после десятичной точки и приведите его в виде a.bcdefghijk.

 Оригинал
'''