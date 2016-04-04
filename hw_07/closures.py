def inc (x):
    return x + 1


#f = inc
#print f(10)

def h(x):
    def g(y):
        return x + y
    return g


def repeat(str):
    def r(times):
        out = ""
        for i in range(times):
            out = out + str
        return out
    return r

r1 = repeat("hello")
r2 = repeat("goodbye")
