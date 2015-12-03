def isValid(x):
    return str(x)[::2] == '1234567890'

def run():
    for x in xrange(1010101010, 1389026624):
        if isValid(x * x):
            return x

if __name__ == "__main__":
    print(run())
