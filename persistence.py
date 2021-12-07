def persistence(n):
    if not n // 10:
        return 0
    else:
        return 1 + persistence(muldigits(n))
    
def muldigits(n):
    if not n // 10:
        return n
    else:
        return n % 10 * muldigits(n // 10)
