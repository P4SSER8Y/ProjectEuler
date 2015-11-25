091 Right triangles with integer coordinates [:link:](http://projecteuler.net/problem=91)  :thought_balloon:
========================

- answer: 14234 
- min used time: 2773 ms

Algorithm
=========

Just brute force it.

Search every pair of points and check if they can form a right angle triangle.

O(n^4) = O(50^4) ¡Ö O(6M) is acceptable. Don't forget to divide the count by 2.