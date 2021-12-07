def disemvowel(string_):
    k = {'A','U','E','O','I'}
    low = {x.lower() for x in k}
    k.update(low)
    return "".join(x for x in string_ if x not in k)
