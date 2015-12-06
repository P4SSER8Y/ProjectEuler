117 Red, green, and blue tiles [:link:](http://projecteuler.net/problem=117)  :clock1::thought_balloon:
========================

- answer: 100808458960497 
- min used time: 0 ms

Algorithm
=========

Classic DP problem. Same as Prob.117.

f[n] denotes the number of ways that combine n blocks.

f[0] = 1

f[n] = sum(f[n - i]), i is the length of tiles.

Time complexity: O(nm)
