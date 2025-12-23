from itertools import combinations

UP, DOWN, LEFT, RIGHT = "UP", "DOWN", "LEFT", "RIGHT"

def get_dir(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if x1 != x2:
        if x2 > x1:
            return RIGHT
        else:
            return LEFT
    else:
        if y2 > y1:
            return DOWN
        else:
            return UP


def solve(fn, part2=False):
    with open(fn) as f:
        lines = [li.strip() for li in f.readlines()]

    #both test and input are clock-wise
    pos = [tuple(int(s) for s in li.split(',')) for li in lines]
    n = len(pos)

    if part2:
        min_pos = min(pos)
        min_pos_ind = pos.index(min_pos)

        #re-sort the pos list so that the top left-most pos is first
        #(meaning we're arriving in the UP direction and exiting in the RIGHT direction)
        pos = pos[min_pos_ind:] + pos[:min_pos_ind]

        in_dirs = [UP,]
        for i in range(1, n):
            in_dirs.append(get_dir(pos[i-1], pos[i]))

        #construct the DMZ
        dmz_set = set()
        for i in range(0,n):
            x1, y1 = pos[i]
            x2, y2 = pos[(i+1)%n]
            in_dir = in_dirs[i%n]
            seg_dir = in_dirs[(i+1)%n] #the direction of the current segment
            out_dir = in_dirs[(i+2)%n]
            #print('going from ', (x1, y1), 'to', (x2, y2), in_dir, seg_dir, out_dir)
            if seg_dir == UP: #dmz is to the left
                for y in range(y2+1, y1):
                    dmz_set.add((x1-1, y))
                if in_dir == LEFT:
                    dmz_set.add((x1-1,y1))
                if out_dir == RIGHT:
                    dmz_set.add((x1-1,y2))
            elif seg_dir == DOWN: #dmz is to the right
                for y in range(y1+1, y2):
                    dmz_set.add((x1+1, y))
                if in_dir == RIGHT:
                    dmz_set.add((x1+1,y1))
                if out_dir == LEFT:
                    dmz_set.add((x1+1,y2))
            elif seg_dir == RIGHT: #dmz is to the top
                for x in range(x1+1, x2):
                    dmz_set.add((x, y1-1))
                if in_dir == UP:
                    dmz_set.add((x1,y1-1))
                if out_dir == DOWN:
                    dmz_set.add((x2,y1-1))
            else: #dmz is to the bottom
                for x in range(x2+1, x1):
                    dmz_set.add((x, y1+1))
                if in_dir == DOWN:
                    dmz_set.add((x1,y1+1))
                if out_dir == UP:
                    dmz_set.add((x2,y1+1))
        print('dmz size:', len(dmz_set))
        #print(dmz_set)

    max_area = 0
    for p1, p2 in combinations(pos, r=2):
        y1, y2 = sorted([p1[1], p2[1]])
        x1, x2 = sorted([p1[0], p2[0]])

        area = (1+y2-y1)*(1+x2-x1)
        if area > max_area:
            if part2:
                #check to see if this rectangle crosses any DMZ
                fail = False
                for x in range(x1, x2+1):
                    if (x,y1) in dmz_set or (x,y2) in dmz_set:
                        fail = True
                        break
                if fail:
                    continue
                for y in range(y1, y2+1):
                    if (x1,y) in dmz_set or (x2,y) in dmz_set:
                        fail = True
                        break
                if fail:
                    continue
                    
            max_area = area

    print(max_area)
    return max_area

def main():
    assert solve('test.txt') == 50
    print(solve('input.txt')) # 4750297200
    assert solve('test.txt', part2=True) == 24 
    print(solve('input.txt', part2=True))

if __name__ == '__main__':
    main()
