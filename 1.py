print('x1 x2 x3 F')
for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            print(x1, x2, x3, x1 or (x2 and x3), sep='  ')
