301 Nim [:link:](http://projecteuler.net/problem=301)  :thought_balloon:
========================

- answer: 2178309 
- min used time: 29029 ms

Algorithm
=========

Game theory's problem: Nim game.

Well, it seemed that i could hardly understand the winning formula. Generally speaking, just calculate each n. If (n xor 2n xor 3n) == 0, the player about to move can win. In other words, X(n, 2n, 3n) = n xor 2n xor 3n.

For more information: [Wiki: Nim:link:](https://en.wikipedia.org/wiki/Nim)
