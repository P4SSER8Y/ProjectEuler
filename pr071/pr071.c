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

bool smaller(long a, long b, long c, long d)
{
	return ((double)a / (double)b) < ((double)c / (double)d);
}

DLL_EXPORT long run(void)
{
	long retN, retD;
	long n, d;
	for (d = 3; d <= 1000000; d++)
	{
		n = (long)3.0*d / 7.0;
		if (smaller(n, d, 3, 7) && smaller(retN, retD, n, d))
		{
			retN = n;
			retD = d;
		}
	}
	return retN;
}

int main(void)
{
	printf("%d\n", run());
    return 0;
}

