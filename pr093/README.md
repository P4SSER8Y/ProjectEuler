093 Arithmetic expressions [:link:](http://projecteuler.net/problem=93)  :thought_balloon:
========================

- answer: 1258 
- min used time: 733 ms

Algorithm
=========

just like the 24-Points-Calculation

1. generate combinations of (1..9)
2. for each combination, generate the permutations
3. for each permutaions, generate the permutations of operators (+-*/) (use truediv instead of div in python 2.7)
4. let . stand for operators, there are two different calculate orders:

	- (((a.b).c).d)
	- ((a.b).(c.d))

well, i was stucked here.
5. just calculate the answer and record the positive integral one.
6. find the n for each combination of (1..9) and get the maximum.

it's really convenient to use itertools and think in functional programming.
Maybe the program consumes more time, but the composing is really fast and clear.
