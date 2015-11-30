080 Square root digital expansion [:link:](http://projecteuler.net/problem=80)  :thought_balloon:
========================

- answer: 40886 
- min used time: 54 ms

Algorithm
=========

the most difficult part is calculating square root with high precision.

Reason
------
1. Let x denote the nearest integer of sqrt(n). (x*10+t) denotes the nearest integer of sqrt(n*100)=sqrt(n)*10. In other word, we want to get each digit step by step.
2. Obviously, we have (x*10+t)^2 <= n*100. As we know, t should be only one digit, so, just calculate it.
3. Let x <- x*10+t, and n <- n * 100 and go on.

