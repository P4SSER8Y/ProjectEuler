import os

while True:
    print("Please enter the new problem's number: ", end = "")
    try:
        n = int(input())
    except:
        print("Wrong Input")
        continue
    break

print("Use C?(y/[n])", end = "")
useC = (input()+' ')[0] in 'yY'

s = 'pr'+str(1000+n)[1:]

if not os.path.exists(s):
    print("Creating folder")
    os.mkdir(s)

print("Creating __init__.py")
f = open(s+r'\__init__.py', 'w')
f.write("from ."+s+" import run as pyRun\n")
if useC:
    f.write("from ctypes import CDLL\n")
    f.write("from os.path import split, realpath\n\n")
    f.write("try:\n")
    f.write("    cRun = CDLL(split(realpath(__file__))[0] + r'\\"+s+".dll').run\n")
    f.write("    cRun.argtypes = None\n    cRun.restype = None\n")
    f.write("except:\n    pass\n")
    f.write("\n#run = pyRun\nrun = cRun\n")
else:
    f.write("\nrun = pyRun\n#run = cRun\n")
f.flush()
f.close()

if not os.path.exists(s+'\\'+s+'.py'):
    print("Creating "+s+".py")
    f = open(s+'\\'+s+'.py', 'w')
    f.write("#coding:utf8\n\n")
    f.write("def "+s+"():\n    pass\n\n")
    f.write("def run():\n    return "+s+"()\n\n")
    f.write('if __name__ == "__main__":\n    print(run())\n')
    f.flush()
    f.close()

if useC:
    if not os.path.exists(s+r'\makefile'):
        print("Creating makefile")
        f = open(s+r'\makefile', 'w')
        f.write("dll:\n\tx86_64-w64-mingw32-gcc "+s+".c -O2 -Wall -shared -o "+s+".dll\n\n")
        f.write("dll:\n\tmingw32-gcc "+s+".c -O2 -Wall -shared -o "+s+"_32.dll\n\n")

        f.write("dll:\n\tgcc "+s+".c -O2 -o "+s+".exe\n\n")
        f.flush()
        f.close()

    if not os.path.exists(s+'\\'+s+'.c'):
        print("Creating "+s+".c")
        f = open(s+'\\'+s+'.c', 'w')
        f.write("""#ifdef _MSC_VER
    #define DLL_EXPORT __declspec(dllexport)
#else
    #define DLL_EXPORT
#endif

#define FOO void

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
    printf("Hello World\\n");
    return 0;
}

""")
        f.flush()
        f.close()
