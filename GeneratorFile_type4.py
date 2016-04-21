import random

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
            if min(testarr) > 0 | max(testarr) < 0:
                testarr = []
                testarr.append(str(numel) + '\n')
        tests.append(' '.join(testarr))
        testarr = []
    return tests
