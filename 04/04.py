import numpy as np
from scipy import ndimage

def solve(fn, part2=False):
    total = 0

    with open(fn) as f:
        lines = [list(li.strip()) for li in f.readlines()]
    
    g = (np.array(lines)=='@').astype(np.uint8)

    kern = np.ones((3,3), dtype=np.uint8)
    kern[1,1] = 0

    while True:
        sum_map = ndimage.convolve(g, kern, mode='constant', cval=0)
        targets = np.logical_and(g, sum_map<4)
        num_removed = np.sum(targets)
        total += num_removed
        g[targets] = 0

        if (not part2) or (num_removed == 0):
            break

    return total

def main():
    assert solve('test.txt') == 13
    print(solve('input.txt'))
    assert solve('test.txt', part2=True) == 43
    print(solve('input.txt', part2=True))

if __name__ == '__main__':
    main()
