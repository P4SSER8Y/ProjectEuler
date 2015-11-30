Observe the formula.

When n is even:

```
  ((a+1)^n+(a-1)^n) mod a^2
= ((p*a^2+n*a+1)+(q*a^2-n*a+1)) mod a^2
= 2 mod a^2
```

So, when n is even, r=2.

Besides, we know that when n is odd, r = 2*n*a mod a^2.

y = 2*n*a is monotonically increasing function. And when 2*n*a = a^2, i.e. n = a/2, r = 0. So, the r_max=2*a*[(a-1)/2]

