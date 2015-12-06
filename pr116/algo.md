Classic DP problem. Same as Prob.117.

f[n] denotes the number of ways that combine n blocks.

f[0] = 1

f[n] = sum(f[n - i]), i is the length of tiles.

Time complexity: O(nm)
