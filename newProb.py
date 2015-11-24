import os

while True:
    print "Please enter the new problem's number:",
    try: 
        n = int(raw_input())
    except:
        print "Wrong Input"
        continue
    break

print "Use C?(y/[n])",
useC = (raw_input()+' ')[0] in 'yY'

s = 'pr'+str(1000+n)[1:]

if not os.path.exists(s):
    print "Creating folder"
    os.mkdir(s)

print "Creating __init__.py"
f = open(s+r'\__init__.py', 'w')
f.write("from "+s+" import run as pyRun\n")
if useC:
    f.write("from ctypes import CDLL\n\n")
    f.write("from os.path import split, realpath\n\n")
    f.write("cRun = CDLL(split(realpath(__file__))[0] + r'\\"+s+".dll').run\n")
    f.write("cRun.argtypes = None\ncRun.restype = None\n\n")
f.write("""
run = pyRun
#run = cRun\n
""")
f.flush()
f.close()

if not os.path.exists(s+'\\'+s+'.py'):
    print "Creating "+s+".py"
    f = open(s+'\\'+s+'.py', 'w')
    f.write("#coding:utf8\n\n")
    f.write("def "+s+"():\n    pass\n\n")
    f.write("def run():\n    return "+s+"()\n\n")
    f.write('if __name__ == "__main__":\n    print run()\n\n')
    f.flush()
    f.close()

if useC:
    if not os.path.exists(s+r'\makefile'):
        print "Creating makefile"
        f = open(s+r'\makefile', 'w')
        f.write("dll:\n\tgcc "+s+".c -O3 -shared -o "+s+".dll\n\n")
        f.write("exe:\n\tgcc "+s+".c -o "+s+".exe\n\n")
        f.flush()
        f.close()

    if not os.path.exists(s+'\\'+s+'.c'):
        print "Creating "+s+".c"
        f = open(s+'\\'+s+'.c', 'w')
        f.write("""#ifdef _MSC_VER
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
    print("Hello World\\n");
    return 0;
}

""")
        f.flush()
        f.close()
