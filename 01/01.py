def solve(fn, part2=False):
    with open(fn) as f:
        lines = f.readlines()

    p = 50
    total = 0

    for li in lines:
        d = int(li[1:])
        if li[0] == 'L':
            d = -d
        if not part2:
            p = (p+d)%100
            if p == 0:
                total += 1
        else:
            if p==0 and d<0:
                total -= 1
            p += d
            total += abs(p//100)
            p = p%100
            if d < 0:
                total += p==0

    return total

def main():
    assert solve('test.txt') == 3
    print(solve('input.txt'))
    assert solve('test.txt', part2=True) == 6
    print(solve('input.txt', part2=True))

if __name__ == '__main__':
    main()
