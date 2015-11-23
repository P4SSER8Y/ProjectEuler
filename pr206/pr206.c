#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#define int64 long long

bool isValid(int64 n)
{
    long k;
    if (n % 10 != 0)
        return false;
    k = 0;
    while (n)
    {
        k = k * 10 + n % 10;
        n /= 100;
    }
    return (k == 987654321);
}

int64 run(void)
{
    int64 x, min, max;
    min = floor(sqrt((int64)1020304050607080900));
    max = floor(sqrt((int64)1929394959697989990));
    for (x = min; x <= max; x++)
        if (isValid(x * x))
            return x;
    return 0;
}

int main(void)
{
    printf("%d\n", run());
    return 0;
}

