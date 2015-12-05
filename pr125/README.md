125 Palindromic sums [:link:](http://projecteuler.net/problem=125)  :thought_balloon:
========================

- answer: 2906969179 
- min used time: 3476 ms

Algorithm
=========

1. Let s[n]=sum(i^2, 0, n), then i^2 + (i+1)^2+ ... + j^2 = s[j] - s[i-1].
2. Just brute force it.
3. Don't forget that there might be numbers who have different form of sum.
