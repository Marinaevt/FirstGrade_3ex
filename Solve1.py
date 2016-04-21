import random

def solve(dataset):
    a = dataset.split()
    arr = a[1:]
    arrborder = [arrborder for arrborder in arr if arrborder > 0]
    return(str(max(arrborder)))
def generate():
    tests = []
    testarr = []
    numtest = 100
    for i in range(numtest):
        numel = random.randint(5, 100)
        testarr.append(str(numel) + '\n')
        while min(testarr) > 0 | max(testarr) < 0:
            for j in range(numel):
                el = random.randint(-1000, 1000)
                testarr.append(str(el) + '\n')
            if min([int(a) for a in testarr]) > 0 | max([int(b) for b in testarr]) < 0:
                testarr = []
                testarr.append(str(numel) + '\n')
        tests.append(' '.join(testarr))
        testarr = []
    return tests
def check(reply, clue):
    if reply == clue:
        return 1
    else:
        return 0