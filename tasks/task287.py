'''
Задача 287
Кодирование квадрадерева (простой алгоритм сжатия)

Кодирование квадрадерева позволяет нам представить черно-белое изображение размерами 2N×2N в виде последовательности битов (0 и 1). Такие последовательности
считываются слева направо следующим образом:
первый бит относится ко всему блоку размерами 2N×2N;
"0" используется в качестве разделителя:обрабатываемый блок размерами 2n×2n делится на 4 подблока размерами 2n-1×2n-
1 каждый,
а последующие биты описывают верхний левый, верхний правый, нижний левый и нижний правый под-блоки -
причем, именно в указанном порядке;"10" указывает на то, что текущий блок содержит только черные
пиксели;
"11" указывает на то, что текущий блок содержит только белые пиксели.
Рассмотрим следующее изображение размерами 4×4 (цветными отметками
указаны места, в которых можно осуществить деление на подблоки):

Это изображение можно описать различными последовательностями, к примеру:"001010101001011111011010101010",
длиною 30 символов, или же
"0100101111101110",
длиною 16 символов, и это - самая короткая возможная последовательность для заданного изображения.
Для натурального числа N определим DN, как изображение размерами 2N×2N со следующей цветовой палитрой:
пиксель с координатами x = 0, y = 0
соответствует самому нижнеми левому пикселю,
если (x - 2N-
1)2 + (y -
 2N-1)2 ≤ 22N-2 то
пиксель окрашен в черный цвет,
в противном случае пиксель окрашен в белый цвет.
Какова длина самой короткой последовательности, описывающей изображение D24 ?
 Оригинал
'''