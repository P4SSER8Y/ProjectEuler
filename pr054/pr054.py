import re
from os.path import split, realpath

HIGH_CARD = 1
ONE_PAIR = 2
TWO_PAIR = 3
THREE_OF_A_KIND = 4
STRAIGHT = 5
FLUSH = 6
FULL_HAUSE = 7
FOUR_OF_A_KIND = 8
STRAIGHT_FLUSH = 9
ROYAL_FLUSH = 10
CARD_VALUE = {'2': 2, '3': 3, '4': 4, '5': 5,
             '6': 6, '7': 7, '8': 8, '9': 9,
             'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def getRank(card):
    def isFlush():
        return card[0][1] == card[1][1] and card[1][1] == card[2][1] and \
               card[2][1] == card[3][1] and card[3][1] == card[4][1]
    def isStraight():
        return (card[0][0] + 1== card[1][0]) and (card[1][0] + 1 == card[2][0]) and \
               (card[2][0] + 1== card[3][0]) and (card[3][0] + 1 == card[4][0])
    def groupByValue():
        d = {}
        for c in card:
            d[c[0]] = d.get(c[0], '') + c[1]
        return d
    cmpCardValue = lambda x, y: x[0] - y[0]
    card.sort(cmp = cmpCardValue)
##ROYAL_FLUSH
    if isFlush() and isStraight() and card[0][0] == CARD_VALUE['A']:
        return ROYAL_FLUSH, card.reverse()
##STRAIGHT_FLUSH
    if isFlush() and isStraight():
        return STRAIGHT_FLUSH, card.reverse()
##FOUR_OF_A_KIND
    group = groupByValue()
    rankStyle = ''.join(sorted([str(len(group[x])) for x in group.keys()], reverse=True))
    if rankStyle == '41':
        t4 = [x for x in group.keys() if len(group[x]) == 4][0]
        return FOUR_OF_A_KIND, [x for x in card if x[0] == t4] + [x for x in card if x[0] != t4]
##FULL_HAUSE
    if rankStyle == '32':
        t3 = [x for x in group.keys() if len(group[x]) == 3][0]
        t2 = [x for x in group.keys() if len(group[x]) == 2][0]
        return FULL_HAUSE, [x for x in card if x[0] == t3] + [x for x in card if x[0] == t2]
##FLUSH
    if isFlush():
        return FLUSH, sorted(card, cmp = cmpCardValue, reverse = True)
##STRAIGHT
    if isStraight():
        return STRAIGHT, sorted(card, cmp = cmpCardValue, reverse = True)
##THREE_OF_A_KIND
    if rankStyle == '311':
        t3 = [x for x in group.keys() if len(group[x]) == 3][0]
        c1 = [x for x in card if x[0] == t3]
        c2 = sorted([x for x in card if x[0] != t3], cmp = cmpCardValue, reverse = True)
        return THREE_OF_A_KIND, c1 + c2
##TWO_PAIR
    if rankStyle == '221':
        t2 = [x for x in group.keys() if len(group[x]) == 2]
        c1 = sorted([x for x in card if x[0] in t2], cmp = cmpCardValue, reverse = True)
        c2 = [x for x in card if not x[0] in t2]
        return TWO_PAIR, c1 + c2 
##ONE_PAIR
    if rankStyle == '2111':
        t2 = [x for x in group.keys() if len(group[x]) == 2][0]
        c1 = [x for x in card if x[0] == t2]
        c2 = sorted([x for x in card if x[0] != t2], cmp = cmpCardValue, reverse = True)
        return ONE_PAIR, c1 + c2
##HIGH_CARD
    if rankStyle == '11111':
        return HIGH_CARD, sorted(card, cmp = cmpCardValue, reverse = True)
##ERROR
    raise NotImplementedError

def aWin(a, b):
    a, b = getRank(a), getRank(b)
    if a[0] > b[0]:
        return True
    if a[0] == b[0]:
        for x in range(len(a[1])):
            if a[1][x][0] > b[1][x][0]:
                return True
            if a[1][x][0] < b[1][x][0]:
                return False
    return False

def run():
    cnt = 0
    f = open(split(realpath(__file__))[0] + "\\data054.txt", 'r')
    for game in f.xreadlines():
        cards =  [(CARD_VALUE[x[0]], x[1]) for x in re.findall(r'\S\S', game)]
        cardA, cardB = cards[:5], cards[5:]
        if aWin(cardA, cardB):
            cnt += 1
    f.close()
    return cnt

if __name__ == "__main__":
    print run()