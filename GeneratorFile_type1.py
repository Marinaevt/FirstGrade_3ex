import random

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
        y = random.randint(-1000, 1000)
        while y < min(testarr):
            y = random.randint(-1000, 1000)
        testarr.append(str(y) + '\n')
        tests.append(' '.join(testarr))
        testarr = []
    return tests
