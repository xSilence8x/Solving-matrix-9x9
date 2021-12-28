# this code is looking for values of given variables
# there are 10 variables with 10 different values from 0 to 9
# every value can be used only once
# our task is to get matrix variables values that has determinant detM = 27182818

import numpy as np
import random

while True:

    numbers = [2, 3, 4, 5, 6, 7, 8, 9]

# variables values of m and my are already known
    m = 0
    my = 1

# the rest of values are searched using random choice from list numbers
    t = random.choice(numbers)
    numbers.remove(t)
    l = random.choice(numbers)
    numbers.remove(l)
    w = random.choice(numbers)
    numbers.remove(w)
    we = random.choice(numbers)
    numbers.remove(we)
    c = random.choice(numbers)
    numbers.remove(c)
    e = random.choice(numbers)
    numbers.remove(e)
    v = random.choice(numbers)
    numbers.remove(v)
    ev = random.choice(numbers)
    numbers.remove(ev)

# matrix of known position of the variables
    matrix = np.array([[ev, w, w, c, l, ev, my, l, v],
                        [w, m, v, t, we, my, t, my, m],
                        [w, v, v, e, t, l, c, we, m],
                        [c, t, e, v, we, w, m, l, my],
                        [l, we, t, we, e, e, ev, w, e],
                        [ev, my, l, w, e, t, t, e, c],
                        [my, t, c, m, ev, t, my, m, ev],
                        [l, my, we, l, w, e, m, l, we],
                        [v, m, m, my, e, c, ev, we, c]])
    print(matrix)

# counting determinant of the matrix
    det = np.linalg.det(matrix)
    det = int(det)
    print(det)

# I assume there can be deviation in calculated solution
# following if statement checkes if our determinant det is in my given range
# the range is +-3 of detM
    if det in range (27182815, 27182821):
        print("Heureka!!")
        break
