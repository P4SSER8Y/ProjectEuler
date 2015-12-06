Kind of like the sieve method for primes.

~~~
f[n] = 0
for i = 1 to n
    j = i
	while j < n
	    f[j]++
		j += i
~~~
