from math import dist, inf, prod
import numpy as np

def solve(fn, connect_limit):
    with open(fn) as f:
        lines = [li.strip() for li in f.readlines()]

    pos = [[int(s) for s in li.split(',')] for li in lines]
    n = len(pos)

    dists = np.ndarray(shape=(n,n), dtype=float)
    set_dict = {i: {i} for i in range(n)}
    num_sets = n
    for r in range(n):
        for c in range(n):
            if r==c:
                dists[r,c] = inf
            elif r<c:
                dists[r,c] = dist(pos[r], pos[c])
            else:
                dists[r,c] = dists[c,r]

    num_connects = 0
    while True:
        i = np.argmin(dists)
        r,c = np.unravel_index(i, shape=(n,n))
        d = dists[r,c]
        assert d != inf #something weird happened
        dists[r,c] = dists[c,r] = inf

        set_a = set_dict[r]
        set_b = set_dict[c]
        if set_a != set_b:
            new_set = set_a.union(set_b)
            for j in new_set:
                set_dict[j] = new_set
            num_sets -= 1

            if num_sets <= 1:
                cable_choice = pos[r][0]*pos[c][0]
                return cable_choice #part 2 return

        num_connects += 1
        if num_connects >= connect_limit:
            break

    circuits = set(tuple(s) for s in set_dict.values())
    c_lens = sorted(len(c) for c in circuits)

    return prod(c_lens[-3:]) #part 1 return

def main():
    assert solve('test.txt', 10) == 40
    print(solve('input.txt', 1000))
    assert solve('test.txt', inf) == 25272
    print(solve('input.txt', inf))

if __name__ == '__main__':
    main()
