def solve(fn, part2=False):
    total = 0

    with open(fn) as f:
        lines = [li.strip() for li in f.readlines()]

    ranges = list()
    ingredients = list()

    for li in lines:
        if '-' in li:
            low, high = [int(s) for s in li.split('-')]
            ranges.append([low, high])
        elif li:
            ingredients.append(int(li))

    if not part2:
        for ing in ingredients:
            for low, high in ranges:
                if low <= ing <= high:
                    total += 1
                    break
    else:
        old_ranges = sorted(ranges)
        ranges = [old_ranges[0]]
        for b_low, b_high in old_ranges[1:]:
            a_low, a_high = ranges[-1]
            if b_low <= a_high:
                #merge
                ranges[-1][1] = max(a_high, b_high)
            else:
                #new entry
                ranges.append([b_low, b_high])
        for low, high in ranges:
            total += high-low+1

    return total

def main():
    assert solve('test.txt') == 3
    print(solve('input.txt'))
    assert solve('test.txt', part2=True) == 14
    print(solve('input.txt', part2=True))

if __name__ == '__main__':
    main()
