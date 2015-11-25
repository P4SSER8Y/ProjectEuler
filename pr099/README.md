099 Largest exponential [:link:](http://projecteuler.net/problem=99)  :clock1::thought_balloon:
========================

- answer: 709 
- min used time: 2 ms

Algorithm
=========

algorithm 0
-----------
calculate the exact number for each pair of numbers. However it's not computable.

algorithm 1
-----------
define a larger float type. Reload the multiply operator and define a quick power function. It's easy to do that.

It's really quick, using less than 1s. But it can't get the right number, which maybe because of the precision.

algorithm 2
-----------
as we know, the log function is increasing when the base > 1. And log(x^y)=y*log(x).

Therefore, we could just compare the y*log(x) and get the line number. The exact number is useless.

This algorithm is much faster then the one above.
