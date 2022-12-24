def day9():
    with open("./input9.txt", "r") as file:
        lines = [line.strip().split(" ") for line in file.readlines()]

        row = {'L': 0, 'U': -1, 'R': 0, 'D': 1}
        col = {'L': -1, 'U': 0, 'R': 1, 'D': 0}

        # part 1
        head = (0, 0)
        tail = (0, 0)
        visited_1 = {(0, 0)}

        for line in lines:
            for i in range(int(line[1])):

                head = (head[0] + row[line[0]], head[1] + col[line[0]])

                dr = head[0] - tail[0]
                dc = head[1] - tail[1]

                if abs(dr) >= 2 and abs(dc) >= 2:
                    tail = (head[0] - 1 if tail[0] < head[0] else head[0] + 1,
                            head[1] - 1 if tail[1] < head[1] else head[1] + 1)
                elif abs(dr) >= 2:
                    tail = (head[0] - 1 if tail[0] < head[0] else head[0] + 1, head[1])
                elif abs(dc) >= 2:
                    tail = (head[0], head[1] - 1 if tail[1] < head[1] else head[1] + 1)

                visited_1.add(tail)

        print(len(visited_1))

        # part 2
        head = (0, 0)
        tails = [(0, 0) for _ in range(9)]
        visited_2 = {(0, 0)}

        for line in lines:
            for i in range(int(line[1])):
                head = (head[0] + row[line[0]], head[1] + col[line[0]])
                tails[0] = recalculate(head, tails[0])
                for j in range(1, 9):
                    tails[j] = recalculate(tails[j - 1], tails[j])

                visited_2.add(tails[8])

        print(len(visited_2))


def recalculate(p1, p2):
    dr = p1[0] - p2[0]
    dc = p1[1] - p2[1]

    if abs(dr) >= 2 and abs(dc) >= 2:
        p2 = (p1[0] - 1 if p2[0] < p1[0] else p1[0] + 1,
              p1[1] - 1 if p2[1] < p1[1] else p1[1] + 1)
    elif abs(dr) >= 2:
        p2 = (p1[0] - 1 if p2[0] < p1[0] else p1[0] + 1, p1[1])
    elif abs(dc) >= 2:
        p2 = (p1[0], p1[1] - 1 if p2[1] < p1[1] else p1[1] + 1)

    return p2


if __name__ == "__main__":
    day9()
