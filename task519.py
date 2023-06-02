'''
Задача 519
Фонтаны трехцветных монет

Монеты, расположенные в один или несколько рядов так, что нижний ряд сплошной (без пропусков), и каждая монета в ряду выше касается ровно двух монет ряда под ним, называются фонтаном монет. Пусть f(n) будет количеством возможных фонтанов из n монет. Для 4 монет существует три возможных фонтана:

Поэтому f(4) = 3, в то время, как f(10) = 78.
Пусть T(n) будет количеством всех возможных раскрасок тремя цветами для всех f(n) существующих фонтанов из n монет, при условии, что никакие две соприкасающиеся монеты не раскрашены в один и тот же цвет. Ниже приведены все возможные раскраски для одного из фонтанов из 4 монет:

Известно, что T(4) = 48 и T(10) = 17760.
Найдите последние 9 цифр в T(20000).
 Оригинал
'''