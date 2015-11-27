387 Harshad Numbers [:link:](http://projecteuler.net/problem=387)  :thought_balloon:
========================

- answer: 696067597313468 
- min used time: 964 ms

Algorithm
=========

1. generate Harshad Number:
    + add a digit to the end and check it, step by step
2. check the number. If it's a strong harshad number, continue.
3. add a digit, check if it's a valid answer
4. add up and print the sum

P.S. to check if it's a prime number, we should use Miller-Rabin algorithms. using a in [2, 3, 7, 11, 61, 24251] is okay (for n <= 1e16).
