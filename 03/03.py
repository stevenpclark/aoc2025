def solve(fn, part2=False):
    total = 0

    if part2:
        num_batts = 12
    else:
        num_batts = 2

    with open(fn) as f:
        lines = [li.strip() for li in f.readlines()]

    for li in lines:
        nums = [int(c) for c in li]
        joltage = 0
        for b in range(num_batts):
            buffer = num_batts-b-1
            v = max(nums[:len(nums)-buffer])
            joltage = joltage*10 + v
            nums = nums[nums.index(v)+1:]
        total += joltage

    return total

def main():
    assert solve('test.txt') == 357
    print(solve('input.txt'))
    assert solve('test.txt', part2=True) == 3121910778619
    print(solve('input.txt', part2=True))

if __name__ == '__main__':
    main()
