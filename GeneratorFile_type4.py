def generate():
    tests = []
    testarr = []
    numtest = 100
    flag1 = 0
    flag2 = 0
    flag3 = 0
    flag7 = 0
    flag13 = 0
    for i in range(numtest):
        numel = random.randint(5, 100)
        testarr.append(str(numel) + '\n')
        while ((min([int(a) for a in testarr]) > 0) | (max([int(b) for b in testarr]) < 0)):
            for j in range(numel):
                el = random.randint(-1000, 1000)
                if flag1 == 0:
                    while el % 2 == 0:
                        el = random.randint(-1000, 1000)
                    testarr.append(str(el) + '\n')
                    flag1 = 1
                elif flag2 == 0:
                    while el % 2 != 0:
                        el = random.randint(-1000, 1000)
                    testarr.append(str(el) + '\n')
                    flag2 = 1
                elif flag3 == 0:
                    while el % 3 != 0:
                        el = random.randint(-1000, 1000)
                    testarr.append(str(el) + '\n')
                    flag3 = 1
                elif flag7 == 0:
                    while el % 7 != 0:
                        el = random.randint(-1000, 1000)
                    testarr.append(str(el) + '\n')
                    flag7 = 1
                elif flag13 == 0:
                    while el % 13 != 0:
                        el = random.randint(-1000, 1000)
                    testarr.append(str(el) + '\n')
                    flag13 = 1
                testarr.append(str(el) + '\n')
            #if min([int(a) for a in testarr]) > 0 | max([int(b) for b in testarr]) < 0:
            #    testarr = []
            #    testarr.append(str(numel) + '\n')
        tests.append(' '.join(testarr))
        testarr = []
    return tests
