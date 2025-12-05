def solve(fn, part2=False):
    total = 0

    with open(fn) as f:
        s = f.read()

    chunks = s.split(',')

    for chunk in chunks:
        low, high = chunk.split('-')
        low = int(low)
        high = int(high)

        for i in range(low, high+1):
            s = str(i)
            s_len = len(s)
            if part2:
                max_repeats = s_len
            else:
                max_repeats = 2
            for n in range(2,max_repeats+1):
                if s_len % n != 0:
                    continue
                fragment = s[0:s_len//n]
                if s == fragment*n:
                    total += i
                    break

    return total

def main():
    assert solve('test.txt') == 1227775554
    print(solve('input.txt'))
    assert solve('test.txt', part2=True) == 4174379265
    print(solve('input.txt', part2=True))

if __name__ == '__main__':
    main()
