for A in range (0, 300):
    c = 0

    for x in range (0, 300):
        for y in range (0, 300):
            if ((4*x + 3*y < A) or (x > y) or (y > 13)):

                c += 1
    if c == 90000:
            print (A)
            break