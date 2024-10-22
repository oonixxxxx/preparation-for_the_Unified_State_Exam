for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                s = not(x <= (y == w)) or (z <= (x == y))
                if s == 0:
                    print(x, w, z, y)