def generate(cur, left, right, n):
    if len(cur)==2*n:
        print (cur)
        return
    if right < left:
        generate(cur + ')', left, right + 1, n)
    if left < n:
        generate(cur + '(', left + 1, right, n)
def parens(n):
    generate('', 0, 0, n)
