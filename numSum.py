with open('input.txt', 'r') as text:
    inp_string = text.readline()
    x, y = inp_string.split(' ')
    sum = int(x) + int(y)
    with open('output.txt', 'w') as out:
        out.write(str(sum))
