179 Consecutive positive divisors [:link:](http://projecteuler.net/problem=179)  :thought_balloon:
========================

- answer: 986262 
- min used time: 2229 ms

Algorithm
=========

Kind of like the sieve method for primes.

~~~
f[n] = 0
for i = 1 to n
    j = i
	while j < n
	    f[j]++
		j += i
~~~
