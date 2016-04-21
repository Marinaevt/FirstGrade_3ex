import random

fex = open('exercise.txt', 'w')
fslv = open('Solve.py', 'w')
mtype = random.randint(1, 2)
typeex = random.randint(1, 4)
ztype = random.randint(1, 2)
mname = ['max(b1,..., bi)', 'min(b1,..., bi)']
fex.write(mname[mtype] + ', ')

if typeex == 1:
    znak = ['bi <= Y', 'bi < Y']
    slvznak = ['<=', '<']
    fex.write(znak[ztype] + '\n')
elif typeex == 2:
    znak = ['X <= bi', 'X < bi']
    slvznak = ['<=', '<']
    fex.write(znak[ztype] + '\n')
elif typeex == 3:
    ztype = random.randint(1, 4)
    znak = ['X < bi < Y', 'X < bi <= Y', 'X <= bi < Y', 'X <= bi <= Y']
    fex.write(znak[ztype] + '\n')
else:
    znak = ['bi < 0', 'bi > 0']
    fex.write(znak[ztype] + '\n')
fgen = open('GeneratorFile_type' + str(typeex) + '.py', 'r')
for line in fgen:
    fslv.write(line)

fslv.write('def solve(dataset):\n')
fslv.write('    arr = map(int, dataset.split())\n')
fex.close()
fslv.close()
fgen.close()