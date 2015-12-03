"""
找规则
"""

def pr028():
    ret = 1
    for k in range(3, 1002, 2):
        ret += 4 * k * k - 6 * k + 6
    return ret 

def run():
    return pr028()

if __name__ == "__main__":
    print(run())

