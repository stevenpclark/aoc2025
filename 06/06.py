from math import prod

op_dict = {'+':sum, '*':prod}

def solve(fn, part2=False):
    total = 0

    with open(fn) as f:
        raw_lines = f.readlines()

    if not part2:
        lines = [li.strip().split() for li in raw_lines]
        ops = lines[-1]
        rows = lines[:-1]

        for i, op in enumerate(ops):
            op_func = op_dict[op]
            col = [int(row[i]) for row in rows]
            total += op_func(col)
    else:
        ops = raw_lines[-1]
        rows = raw_lines[:-1]
        nc = len(ops) 
        nums = []
        c = nc-2
        while c >= 0:
            num = int(''.join([row[c] for row in rows]))
            nums.append(num)
            op_char = ops[c]
            if op_char != ' ':
                op_func = op_dict[op_char]
                total += op_func(nums)
                nums = []
                c -= 1
            c -= 1

    return total

def main():
    assert solve('test.txt') == 4277556
    print(solve('input.txt'))
    assert solve('test.txt', part2=True) == 3263827
    print(solve('input.txt', part2=True))

if __name__ == '__main__':
    main()
