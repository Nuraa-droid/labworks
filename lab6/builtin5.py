def ttt(tup):
    return all(tup)

tup = input()
tup = tuple(map(str.strip, tup.split(",")))
cnvrt = tuple(bool(elem) for elem in tup)
print(ttt(cnvrt))