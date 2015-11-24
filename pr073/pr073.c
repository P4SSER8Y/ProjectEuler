#ifdef _MSC_VER
    #define DLL_EXPORT __declspec(dllexport)
#else
    #define DLL_EXPORT
#endif

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <math.h>

DLL_EXPORT long run(void);
int main(void);
long gcd(long a, long b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

DLL_EXPORT long run(void)
{
    long ret;
    long x, y;
    ret = 0;
    for (x = 4; x <= 12000; x++)
        for (y = (long)(x/3)+1; y < (x >> 1) + (x & 1); y++)
            if (gcd(x, y) == 1)
                ret ++;
    return ret; 
}

int main(void)
{
    printf("%d\n", run());
    return 0;
}

