import re

def pr017():
    ones = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10: 'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
    tens = {1:'ten', 2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}
    def toEnglish(x):
        ret = ''
        if x >= 100:
            ret += ones[x // 100 % 10] + ' hundred'
            if x % 100 > 0:
                ret += ' and '
        x = x % 100
        if x >= 20:
            ret += tens[x // 10]
            if x % 10 > 0:
                ret += '-' + ones[x % 10]
        else:
            ret += ones[x]
        return ret

    ret = len(re.sub(r'[^a-z]', '', 'one thousand'))
    for x in range(1, 1000):
        s = toEnglish(x)
        cnt = len(re.sub(r'[^a-z]', '', s))
        ret += cnt
    return ret

def run():
    return pr017()

if __name__ == "__main__":
    print(run())

