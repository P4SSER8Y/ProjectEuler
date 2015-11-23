#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <math.h>

long* getPrimes(long n)
{
    long i, j, cnt;
    bool* flag;
    long* ret;

    flag = calloc(n + 1, sizeof(bool));
    for (i = 0; i <= n; i++)
        flag[i] = true;
    flag[0] = false; flag[1] = false;
    i = 2; cnt = 0;
    while (i <= n)
    {
        while ((i <= n) && (!flag[i])) i++;
        if (i > n) break;
        cnt++;
        j = 2 * i;
        while (j <= n)
        {
            flag[j] = false;
            j += i;
        }
        i++;
    }
    ret = calloc(cnt, sizeof(long));
    i = 0; j = 0;
    while (i < cnt)
    {
        while (!flag[j]) j++;
        ret[i++] = j++;
    }
    free(flag);
    return ret;
}

long* getPrimes_2(long n)
{
    long i, j, cnt;
    bool* flag;
    long* ret;

    flag = calloc(n + 1, sizeof(bool));
    for (i = 0; i <= n; i++)
        flag[i] = true;
    flag[0] = false; flag[1] = false;
    i = 2; cnt = 0;
    while (i <= n)
    {
        while ((i <= n) && (!flag[i])) i++;
        if (i > n) break;
        cnt++;
        j = 2 * i;
        while (j <= n)
        {
            flag[j] = false;
            j += i;
        }
        i++;
    }
    ret = calloc(cnt + 1, sizeof(long));
    ret[0] = cnt;
    i = 1; j = 0;
    while (i <= cnt)
    {
        while (!flag[j]) j++;
        ret[i++] = j++;
    }
    free(flag);
    return ret;
}

/*
 *long pow(long a, long n)
 *{
 *    if (n == 0)
 *        return 1;
 *    if (n == 1)
 *        return a;
 *    if (n & 1)
 *        return pow(a * a, n >> 1) * a;
 *    else
 *        return pow(a * a, n >> 1);
 *}
 */

long phi(long n, long* primes)
{
    long cnt, i, ret;
    i = 0;
    ret = 1;
    while (n > 1)
    {
        while (n % primes[i]) i++;
        cnt = 0;
        while (!(n % primes[i]))
        {
            cnt++;
            n /= primes[i];
        }
        ret *= pow(primes[i], cnt - 1) * (primes[i] - 1);
    }
    return ret;
}

bool isValid(long a,long b)
{
    char sa[10], sb[10];
    char i;
    for (i = 0; i < 10; i++)
    {
        sa[i] = 0; sb[i] = 0;
    }
    while (a)
    {
        sa[a % 10]++;
        a /= 10;
    }
    while (b)
    {
        sb[b % 10]++;
        b /= 10;
    }
    for (i = 0; i < 10; i++)
        if (sa[i] != sb[i])
            return false;
    return true;
}

long pr070(long n)
{
    long* primes;
    long i;
    long minN, phiX;
    double minValue;

    primes = getPrimes(n);
    minValue = 2147483647;
    minN = 0;
    for (i = 2; i < n; i++)
    {
        phiX = phi(i, primes);
        if (isValid(i, phiX))
        {
            printf("%d\r", i);
            if ((((double)i) / phiX) < minValue)
            {
                minValue = ((double)i) / phiX;
                minN = i;
            }
        }
    }
    printf("\n");
    free(primes);
    return minN;
}

long pr070_2(long n)
{
    long* prime_1, *prime_2;
    long i, j, x, y, phi_2;
    double minValue;
    long minN;

    prime_1 = getPrimes_2(floor(sqrt(n)));
    prime_2 = getPrimes_2(n >> 1);

    minValue = 2147483647;
    minN = 0;
    for (i = 1; i <= prime_1[0]; i++)
        for (j = 1; j <= prime_2[0]; j++)
        {
            x = prime_1[i]; y = prime_2[j];
            if ((x * y > n) || (x * y == 0)) break; 
            phi_2 = (x - 1) * (y - 1);
            if (isValid(x * y, phi_2) && (((double)(x*y) /(double)phi_2) < minValue))
            {
                minN = x * y;
                minValue = (double)(x * y) / (double)phi_2;
            }
        }
    free(prime_1);
    free(prime_2);
    return minN;
}

int main(void)
{
    /*printf("%d", pr070((long)1e7));*/
    printf("%d", pr070_2((long)1e7));
    return 0;
}

long run()
{
    /*return pr070((long)1e7);*/
    return pr070_2((long)1e7);
}
