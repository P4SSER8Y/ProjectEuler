102 Triangle containment [:link:](http://projecteuler.net/problem=102)  :clock1::thought_balloon:
========================

- answer: 228 
- min used time: 33 ms

Algorithm
=========

Geometry problem.

To decide whether P(0,0) in Tri-ABC. We could use cross product (aka. vector product).

1. Calculate ABxAP, BCxBP, and CAxCP.
2. P is in Tri-ABC if and only if these three products have the same symbol.

