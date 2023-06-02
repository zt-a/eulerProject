'''
Задача 591
Наилучшие аппроксимации квадратичными целыми

При данном не являющимся квадратом целом числом $d$ любое вещественное число $x$ может быть аппроксимировано сколько угодно точно с помощью квадратичных целых чисел $a+b\sqrt{d}$, где $a,b$ являются целыми числами. Например, следующие неравенства аппроксимируют $\pi$ с точностью $10^{-13}$:
$$4375636191520\sqrt{2}-6188084046055 < \pi < 721133315582\sqrt{2}-1019836515172 $$ 
Назовем $BQA_d(x,n)$ квадратичное целое, ближайшее к $x$ с абсолютными значениями $a,b$ не превыщающими $n$. Также определим целую часть квадратичного целого как $I_d(a+b\sqrt{d}) = a$.
Известно, что:
$BQA_2(\pi,10) = 6 - 2\sqrt{2}$
$BQA_5(\pi,100)=26\sqrt{5}-55$
$BQA_7(\pi,10^6)=560323 - 211781\sqrt{7}$
$I_2(BQA_2(\pi,10^{13}))=-6188084046055$
Найдите сумму $|I_d(BQA_d(\pi,10^{13}))|$ для всех натуральных чисел меньше 100, не являющихся квадратами.
 Оригинал
'''