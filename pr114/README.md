114 Counting block combinations I [:link:](http://projecteuler.net/problem=114)  :clock1::thought_balloon:
========================

- answer: 16475640049 
- min used time: 0 ms

Algorithm
=========

Dynamic programming. O(n^2) -> O(n)

Let fr[i] denotes when the i-th tile is red, the ways of combination. So as fb[i]. 

Let m denotes the mininum length of red blocks.

1. fr[0] = 0, fb[0] = 1
2. fr[i] = sum(fb[j], 0<=j<=i-m)
3. fb[i] = fr[i-1] + fb[i-1]

To optimize, the second formula could be rewritten as fr[i] = fr[i-1]+fb[i-m] (i-m>=0), fr[i] = 0 (i-m < 0).

So,

1. fr[0] = 0, fb[0] = 1
2. fr[i] = fr[i-1] + fb[i-m], when i >= m
3. fr[i] = 0, when i < m
4. fb[i] = fr[i-1] + fb[i-1]

Therefore, F(m, n) = fr[n] + fb[n].

Hence, the answer to Prob. 114 should be F(3, 50).
