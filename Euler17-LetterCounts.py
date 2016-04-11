#Project Euler problem #17
#Number letter counts
#Jon McMahon, March 2016


NUMS_TO_LETTERS = {1 : 'one',
                   2 : 'two',
                   3 : 'three',
                   4 : 'four',
                   5 : 'five',
                   6 : 'six',
                   7 : 'seven',
                   8 : 'eight',
                   9 : 'nine',
                   10 : 'ten',
                   11 : 'eleven',
                   12 : 'twelve',
                   13 : 'thirteen',
                   14 : 'fourteen',
                   15 : 'fifteen',
                   16 : 'sixteen',
                   17 : 'seventeen',
                   18 : 'eighteen',
                   19 : 'nineteen',
                   20 : 'twenty',
                   30 : 'thirty',
                   40 : 'forty',
                   50 : 'fifty',
                   60 : 'sixty',
                   70 : 'seventy',
                   80 : 'eighty',
                   90 : 'ninty',
                   100 : 'hundred',
                   1000 : 'thousand'}

NUMBER_BASES = {100 : NUMS_TO_LETTERS[100],
                1000 : NUMS_TO_LETTERS[1000]}

NUMBER_SUB_BASES = {n : NUMS_TO_LETTERS[n] for n in NUMS_TO_LETTERS.keys() if n < 100 and n % 10 == 0}


def writeAsLetters(n):
    if n == 0:
        return ''
    for x in sorted(NUMBER_BASES.keys(), reverse = True):
        if n >= x:
            ct = n // x
            if n % x:
                return writeAsLetters(ct) + NUMBER_BASES[x] + 'and' + writeAsLetters(n % x)
            else:
                return writeAsLetters(ct) + NUMBER_BASES[x]
    try:
        return NUMS_TO_LETTERS[n]
    except KeyError:
        for x in sorted(NUMBER_SUB_BASES.keys(), reverse = True):
            if n > x:
                return NUMBER_SUB_BASES[x] + writeAsLetters(n % x)



if __name__ == '__main__':
    print('Answer:', sum(len(writeAsLetters(x)) for x in range(1, 1001)))
