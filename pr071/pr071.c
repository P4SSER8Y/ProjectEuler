#ifdef _MSC_VER
    #define DLL_EXPORT __declspec(dllexport)
#else
    #define DLL_EXPORT
#endif

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <math.h>

DLL_EXPORT FOO run(void);
int main(void);

DLL_EXPORT FOO run(void)
{
    return;
}

int main(void)
{
    print("Hello World\n");
    return 0;
}

