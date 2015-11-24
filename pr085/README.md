[085 Counting rectangles](http://projecteuler.net/problem=85):thought_balloon:
========================

- answer: 2772 
- min used time: 149 ms

Algorithm
=========

1. Every two points may make one rectangles. So there are C(x*y,2) rectangles.
2. The points in the same line could not make rectangels. There are x*C(y,2)+y*C(x,2) pairs.
3. At the same time, one rectangle have two pairs of diagonal points. So the answer should be divided by 2.
4. Therefore, the final formula is x*y*(x-1)*(y-1)/4, in which x=a+1, y=b+1.

The x,y are supposed be near (2000000*4)^0.25=53
