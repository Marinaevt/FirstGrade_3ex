import random

fex = open('exercise.txt', 'w')

numvar = 3
for i in range(numvar):
    fslv = open('Solve' + str(i) + '.py', 'w')
    fslvt = open('SolveTemplate.py', 'r')
    fchk = open('CheckFile.py', 'r')
    typeex = random.randint(1, 4)
    ztype = random.randint(1, 2)
    mname = ['max(bi,..., bj)', 'min(bi,..., bj)', 'mean(bi, ..., bj)', '(bi,...., bj), bk = (i+j)/2']
    moddname = ['bk mod 2 = 0', 'bk mod 2 != 0', 'bk mod 3 = 0', 'bk mod 7 = 0', 'bk mod 13 = 0']
    modd = [' & (arrborder%2==0))]\n', ' & (arrborder%2!=0))]\n', ' & (arrborder%3==0))]\n', ' & (arrborder%7==0))]\n', ' & (arrborder%13==0))]\n']
    moddtype = random.randint(1, len(moddname))
    mtype = random.randint(1, len(mname))
    fex.write(mname[mtype-1] + ', when ')
    for line in fslvt:
        fslv.write(line)
    if typeex == 1:
        znak = ['bk <= Y', 'bk < Y']
        fslv.write('    arr = a[1:-1]\n')
        fslv.write('    Y = a[-1]\n')
        if ztype == 1:
            fslv.write('    arrborder = [arrborder for arrborder in arr if ((arrborder <= Y)')
        else:
            fslv.write('    arrborder = [arrborder for arrborder in arr if ((arrborder < Y)')
        fex.write(znak[ztype-1] + ' and ')
    elif typeex == 2:
        znak = ['X <= bk', 'X < bk']
        fslv.write('    arr = a[1:-1]\n')
        fslv.write('    X = a[-1]\n')
        if ztype == 1:
            fslv.write('    arrborder = [arrborder for arrborder in arr if ((arrborder >= X)')
        else:
            fslv.write('    arrborder = [arrborder for arrborder in arr if ((arrborder > X)')
        fex.write(znak[ztype-1] + ' and ')
    elif typeex == 3:
        ztype = random.randint(1, 4)
        fslv.write('    arr = a[1:-2]\n')
        fslv.write('    X = a[-2]\n')
        fslv.write('    Y = a[-1]\n')
        znak = ['X < bk < Y', 'X < bk <= Y', 'X <= bk < Y', 'X <= bk <= Y']
        fslv.write('    arrborder = [arrborder for arrborder in arr if ')
        if ztype == 1:
            fslv.write('((arrborder > X) & (arrborder < Y)')
        elif ztype == 2:
            fslv.write('((arrborder > X) & (arrborder <= Y)')
        elif ztype == 3:
            fslv.write('((arrborder >= X) & (arrborder < Y)')
        else:
            fslv.write('((arrborder >= X) & (arrborder <= Y)')
        fex.write(znak[ztype-1] + ' and ')
    else:
        znak = ['bk < 0', 'bk > 0']
        fslv.write('    arr = a[1:]\n')
        fslv.write('    arrborder = [arrborder for arrborder in arr if ')
        if ztype == 1:
            fslv.write('((arrborder < 0)')
        elif ztype == 2:
            fslv.write('((arrborder > 0)')
        fex.write(znak[ztype-1] + ' and ')
    fex.write(moddname[moddtype - 1] + '\n')
    fslv.write(modd[moddtype - 1])
    if mtype == 1:
        fslv.write('    return(str(max(arrborder)))\n')
    elif mtype == 2:
        fslv.write('    return(str(min(arrborder)))\n')
    elif mtype == 3:
        fslv.write('    return(str(float(sum(arrborder)/len(arrborder))))\n')
    else:
        fslv.write('    return(str(arrborder[len(arrborder)/2]))\n')
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