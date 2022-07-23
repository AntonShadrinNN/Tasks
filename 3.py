print('x y z F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(x, y, z, 1 if (((x or y) and not x) <= y) and (z or not z) else 0)
