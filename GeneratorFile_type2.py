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
        x = random.randint(-1000, 1000)
        while x > max(testarr):
            x = random.randint(-1000, 1000)
        testarr.append(str(x) + '\n')
        tests.append(' '.join(testarr))
        testarr = []
    return tests
