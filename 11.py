import random
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Y = 5
arrborder = [arrborder for arrborder in a if arrborder <= Y]
print(max(a))
print(max(a[:-3]))
print(min(a[2:]))
print(a[1:-1])
print(arrborder)