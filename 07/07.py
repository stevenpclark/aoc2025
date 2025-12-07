def solve(fn, part2=False):
    total_splits = 0

    with open(fn) as f:
        lines = [li.strip() for li in f.readlines()]

    nc = len(lines[0])
    beams = [0,]*nc
    beams[lines[0].index('S')] = 1

    for li in lines[1:]:
        for c in range(nc):
            if beams[c] and li[c] == '^':
                beams[c-1] += beams[c]
                beams[c+1] += beams[c]
                beams[c] = 0
                total_splits += 1

    if not part2:
        return total_splits
    else:
        return sum(beams)

def main():
    assert solve('test.txt') == 21
    print(solve('input.txt'))
    assert solve('test.txt', part2=True) == 40 
    print(solve('input.txt', part2=True))

if __name__ == '__main__':
    main()
