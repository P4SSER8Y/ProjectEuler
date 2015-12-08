249 Prime Subset Sums [:link:](http://projecteuler.net/problem=249)  :warning::thought_balloon:
========================

- answer: 9275262564250418 
- min used time: 133636 ms

Algorithm
=========

DP.

let f[i, j] is the number of subsets whose sum is i, and the last element is the j-th prime.

Time complexity: O(n*Sp), Sp = sum(primes), n is the number of primes.

Formula:

1. f[0, j] = 1, for all j.
2. f[i, j] = sum(f[i-p[j], k], for 1 <= k < j)

Finally, just sum up all the f[i, j], i is a prime.
