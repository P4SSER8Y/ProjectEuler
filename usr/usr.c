#ifdef _MSC_VER
    #define DLL_EXPORT __declspec(dllexport)
#else
    #define DLL_EXPORT
#endif

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#define int64 long long

int cmpGetFactors(const void *a, const void* b);
DLL_EXPORT long* getPrimeFactors(long n);
DLL_EXPORT long* getFactors(long n);
DLL_EXPORT long* getPrimes(long n);
DLL_EXPORT bool isPrime(long n);
DLL_EXPORT bool isPrimeMR(int64 n);
bool MR_witness(int64 a, int64 n);
int64 powMod(int64 a, int64 d, int64 n);
DLL_EXPORT long gcd(long a, long b);

DLL_EXPORT long gcd(long a, long b)
{
	if (!b)
		return a;
	return gcd(b, a % b);
}

int64 powMod(int64 a, int64 d, int64 n)
{
    if (d == 0)
        return 1;
    if (d == 1)
        return (a % n);
    a %= n;
    if ((d & 1) == 0)
        return powMod(a * a % n, d >> 1, n) % n;
    else
        return powMod(a * a % n, d >> 1, n) * a % n;
}

bool MR_witness(int64 a, int64 n)
{
    int64 d, t;
    if (n == 2)
        return true;
    if ((n == 1) || ((n & 1) == 0))
        return false;
    d = n - 1;
    while ((d & 1) == 0)
        d >>= 1;
    t = powMod(a, d, n);
    while ((d != n - 1) && (t != 1) && (t != n - 1))
    {
        t = (t * t) % n;
        d <<= 1;
    }
    return ((t == n - 1) || ((d & 1) == 1));
}

DLL_EXPORT bool isPrimeMR(int64 n)
{
    const int a[] = {2, 3, 7, 11, 61, 24251};
    int i;
	for (i = 0; i < 6; i++)
		if (a[i] == n)
			return true;
    for (i = 0; i < 6; i++)
        if (!MR_witness(a[i], n))
            return false;
    return true;
}

int cmpGetFactors(const void *a, const void* b)
{
    return *(long*)a - *(long*)b;
}

DLL_EXPORT long* getPrimeFactors(long n)
{
    long *primes, *tmp, *pFactors;
    long i;
    if (isPrimeMR(n))
    {
        pFactors = calloc(2, sizeof(long));
        pFactors[0] = 1;
        pFactors[1] = n;
        return pFactors;
    } 
    primes = getPrimes(n >> 1);
    tmp = calloc(n, sizeof(long));
    tmp[0] = 0;
    for (i = 1; i <= primes[0]; i++)
        if (!(n % primes[i]))
            tmp[++tmp[0]] = primes[i];
    pFactors = calloc(tmp[0]+1, sizeof(long));
    pFactors[0] = tmp[0];
    for (i = 1; i <= tmp[0]; i++)
        pFactors[i] = tmp[i];
    free(tmp);
    free(primes);
    return pFactors;
}

DLL_EXPORT long* getFactors(long n)
{
    long *fac = calloc(n+1, sizeof(long));
    long *ret;
    long i;
    fac[0] = 0;
    for (i=1; i*i<=n; i++)
        if (n % i == 0)
        {
            fac[++fac[0]] = i;
            fac[++fac[0]] = n / i;
        }
    ret = calloc(fac[0] + 1, sizeof(long));
    ret[0] = 0;
    for (i=1; i<=fac[0]; i++)
        ret[i] = fac[i];
    qsort(ret, fac[0] + 1, sizeof(long), cmpGetFactors);
    ret[0] = fac[0];
    free(fac);
    return ret;
}

DLL_EXPORT long* getPrimes(long n)
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

DLL_EXPORT bool isPrime(long n)
{
    long i;
    if (n < 2) return false;
    if ((n & 1) == 0) return false;
    if (n == 2) return true;
    for (i = 3; i * i <= n; i+=2)
        if (n % i == 0)
            return false;
    return true;
}

/*
 *__int64 powerMod(__int64 a, __int64 n, __int64 m)
 *{
 *    __int64 t;
 *    if (n == 0) return 1;
 *    if (n == 1) return (a % m);
 *    t = (a * a) % m;
 *    if (n % 2 == 1)
 *        return (powerMod(t, n >> 1, m) * a) % m;
 *    else
 *        return powerMod(t, n >> 1, m) % m;
 *}
 *
 *DLL_EXPORT bool isPrimeMillerRabin(long n, long a)
 *{
 *    return true;
 *}
 */

