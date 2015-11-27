Brute force. O(n^1.5). With cuts, program stops within 1 min.

Cuts:

1. if it's prime, just ignore it. foo(1) + foo(2) = 3.
2. for each number, calc the d with range(1, sqrt(n)).

