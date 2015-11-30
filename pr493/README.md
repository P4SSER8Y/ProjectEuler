493 Under The Rainbow [:link:](http://projecteuler.net/problem=493)  :thought_balloon:
========================

- answer: 6.81874180202 
- min used time: 407 ms

Algorithm
=========

combinations problem

permutate every possible number for each color. Let [a, b, c, d, e, f, g] denotes the numbers of different colors. The probablity of this combination should be product(C(10, x)), for x in [a,b,c,d,e,f,g]. Then count the number of this combination and multiply it with the probablity. Sum them up and divide it by C(70, 20).

