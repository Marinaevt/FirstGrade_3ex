import random

fex = open('exercise.txt', 'w')

numvar = 3
for i in range(numvar):
    fslv = open('Solve' + str(i) + '.py', 'w')
    fslvt = open('SolveTemplate.py', 'r')
    fchk = open('CheckFile.py', 'r')
    mtype = random.randint(1, 2)
    typeex = random.randint(1, 4)
    ztype = random.randint(1, 2)
    mname = ['max(b1,..., bi)', 'min(b1,..., bi)']
    fex.write(mname[mtype-1] + ', ')
    for line in fslvt:
        fslv.write(line)
    if typeex == 1:
        znak = ['bi <= Y', 'bi < Y']
        fslv.write('    arr = a[1:-1]\n')
        fslv.write('    Y = a[-1]\n')
        if ztype == 1:
            fslv.write('    arrborder = [arrborder for arrborder in arr if arrborder <= Y]\n')
        else:
            fslv.write('    arrborder = [arrborder for arrborder in arr if arrborder < Y]\n')
        fex.write(znak[ztype-1] + '\n')
    elif typeex == 2:
        znak = ['X <= bi', 'X < bi']
        fslv.write('    arr = a[1:-1]\n')
        fslv.write('    X = a[-1]\n')
        if ztype == 1:
            fslv.write('    arrborder = [arrborder for arrborder in arr if arrborder >= X]\n')
        else:
            fslv.write('    arrborder = [arrborder for arrborder in arr if arrborder > X]\n')
        fex.write(znak[ztype-1] + '\n')
    elif typeex == 3:
        ztype = random.randint(1, 4)
        fslv.write('    arr = a[1:-2]\n')
        fslv.write('    X = a[-2]\n')
        fslv.write('    Y = a[-1]\n')
        znak = ['X < bi < Y', 'X < bi <= Y', 'X <= bi < Y', 'X <= bi <= Y']
        fslv.write('    arrborder = [arrborder for arrborder in arr if ')
        if ztype == 1:
            fslv.write('arrborder > X & arrborder < Y]\n')
        elif ztype == 2:
            fslv.write('arrborder > X & arrborder <= Y]\n')
        elif ztype == 3:
            fslv.write('arrborder >= X & arrborder < Y]\n')
        else:
            fslv.write('arrborder >= X & arrborder <= Y]\n')
        fex.write(znak[ztype-1] + '\n')
    else:
        znak = ['bi < 0', 'bi > 0']
        fslv.write('    arr = a[1:]\n')
        fslv.write('    arrborder = [arrborder for arrborder in arr if ')
        if ztype == 1:
            fslv.write('arrborder < 0]\n')
        elif ztype == 2:
            fslv.write('arrborder > 0]\n')
        fex.write(znak[ztype-1] + '\n')
    if mtype == 1:
        fslv.write('    return(str(max(arrborder)))\n')
    else:
        fslv.write('    return(str(min(arrborder)))\n')
    fgen = open('GeneratorFile_type' + str(typeex) + '.py', 'r')
    for line in fgen:
        fslv.write(line)
    for line in fchk:
        fslv.write(line)
    fslv.close()
    fgen.close()
    fslvt.close()
    fchk.close()
fex.close()