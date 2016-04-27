import random

def solve(dataset):
    a = dataset.split()
    arr = a[1:-2]
    X = a[-2]
    Y = a[-1]
    arrborder = [arrborder for arrborder in arr if arrborder > X & arrborder <= Y & arrborder % 2 != 0]
    return(str(min(arrborder)))
def generate():
    tests = []
    testarr = []
    numtest = 100
    for i in range(numtest):
        numel = random.randint(5, 100)
        testarr.append(str(numel) + '\n')
        for j in range(numel):
            el = random.randint(-1000, 1000)
            testarr.append(str(el) + '\n')
        x = random.randint(-1000, 1000)
        y = random.randint(-1000, 1000)
        while x > max([int(a) for a in testarr]) | y < min([int(b) for b in testarr]):
            x = random.randint(-1000, 1000)
            y = random.randint(-1000, 1000)
        testarr.append(str(x) + '\n')
        testarr.append(str(y) + '\n')
        tests.append(' '.join(testarr))
        testarr = []
    return tests
def check(reply, clue):
    if reply == clue:
        return 1
    else:
        return 0