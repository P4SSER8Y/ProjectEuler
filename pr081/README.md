081 Path sum: two ways [:link:](http://projecteuler.net/problem=81)  :clock1::thought_balloon:
========================

- answer: 427337 
- min used time: 37 ms

Algorithm
=========

typical DP problem. O(n^2)

Equations:
1. f[i,j] = min(f[i-1,j] + f[i,j-1]) + v[i,j]
2. f[0,0] = v[0,0]
3. f[i,0] = f[i-1,0]+v[i,0]
4. f[0,j] = f[0,j-1]+v[0,j]

PS. I hate Python's list.
