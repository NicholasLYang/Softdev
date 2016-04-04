# print [x for x in range(8)]

# print [(pow (x, 2), pow((x + 1), 2), pow((x + 2), 2)) for x in range(8)]


p = "myNoobPass1234"

# print [x for x in p]

# print [x for x in "1234"]

NUM = "0123456789"
UC_LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#[ x for x in p if x in UC_LETTERS ]

#print [ 1 for x in p if x in UC_LETTERS ]

# print [ 1 if x in UC_LETTERS else 0 for x in p ] 


def passTest(p):
    out = [1 if x  in UC_LETTERS else 2 if x in NUM else 0 for x in p]
    print out
    return  all(x in out for x in [0, 1, 2])


# Length: any password above 16 digits is "strong", any password below 6 is "weak"
# Characters: For every new type of character, doubles strength

CHAR = "!@#$%^&*();,.<>-_=+[]{}:'?/`~`"


def passStrength(p):
    length = len(p)
    print length
    if length > 19:
        return 5
    if length < 8:
        return 0
    parse  = [1 if x in UC_LETTERS else 2 if x in NUM else 3 if x in CHAR else 0 for x in p]
    out = length/ 5
    bonus = 1
    if 1 in parse:
        out = out + bonus
        bonus = bonus * 2
    if 2 in parse:
        out = out + bonus
        bonus = bonus * 2
    if 3 in parse:
        out = out + bonus
        bonus = bonus * 2
    if out >= 5:
        return 5
    return int(out)



