#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

long* getPrimes(long n)
{
    bool* flag = calloc(n+1, sizeof(bool));
    long* ret;
    long i, j;
    long cnt;

    flag[0]=false; flag[1]=false;
    for (i=2; i<=n; i++) flag[i]=true;
    i=2;
    cnt = 0;
    while (i <= n)
    {
        while ((i <= n) && (!flag[i])) i++;
        if (i > n) break;
        cnt++;
        for (j = 2*i; j <= n; j += i)
            flag[j] = false;
        i++;
    }
    ret = calloc(cnt+1, sizeof(long));
    ret[0] = cnt;
    j = 0; i = 1;
    while (++j <= n)
        if (flag[j])
            ret[i++] = j;
    return ret;
}

long phi(long n, long* primes)
{
    long long ret;
    long k;

    ret = n;
    for (k = 1; k <= primes[0]; k++)
    {
        if (primes[k] > n)
            break;
        if (n % primes[k] == 0)
        {
            ret /= primes[k];
            ret *= primes[k] - 1;
        }
    }
    return ret;
}

long long run()
{
    long long ret;
    long k;
    long *primes;
    primes = getPrimes((long)1e6);
    ret = 0;
    for (k = 2; k <= (long)1e6; k++)
        ret += phi(k, primes);
    free(primes);
    return ret;
}

int main(void)
{
    printf("%ld\n", run());
    return 0;
}

