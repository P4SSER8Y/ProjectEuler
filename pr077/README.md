077 Prime summations [:link:](http://projecteuler.net/problem=77)  :clock1::thought_balloon:
========================

- answer: 71 
- min used time: 2 ms

Algorithm
=========

Classic DP.

The time complexity is O(n^2).

Let f[n] denotes the numbers of ways of n, f[i] = sum(f[i-j]), j is a prime number.

