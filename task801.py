'''
Задача 801
$x^y \equiv y^x$

Положительными целыми корнями уравнения $x^y=y^x$ являются $(2,4)$, $(4,2)$ и $(k,k)$ для всех $k > 0$.
Для данного положительного целого числа $n$ пусть $f(n)$ будет количеством целочисленных значений $0 < x,y \leq n^2-n$, таких что
$$x^y\equiv y^x \pmod n$$
Например, $f(5)=104$ и $f(97)=1614336$.
Пусть $S(M,N)=\sum f(p)$, где сумма взята по всем простым числам $p$, удовлетворяющим $M\le p\le N$.
Известно, что $S(1,10^2)=7381000$ и $S(1,10^5) \equiv 701331986 \pmod{993353399}$.
Найдите $S(10^{16}, 10^{16}+10^6)$. В качестве ответа приведите остаток от деления полученного результата на $993353399$.
 Оригинал
'''