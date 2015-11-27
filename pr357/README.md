357 Prime generating integers [:link:](http://projecteuler.net/problem=357)  :thought_balloon:
========================

- answer: 1739023853137 
- min used time: 47792 ms

Algorithm
=========

Brute force. O(n^1.5). With cuts, program stops within 1 min.

Cuts:

1. if it's prime, just ignore it. foo(1) + foo(2) = 3.
2. for each number, calc the d with range(1, sqrt(n)).

