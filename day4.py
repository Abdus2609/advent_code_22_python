def day4():
    result_1 = 0
    result_2 = 0
    with open("./day4input.txt", "r") as file:
        lines = [line.strip().split(",") for line in file.readlines()]
        for line in lines:
            (start1, end1, start2, end2) = (
                int(line[0].split('-')[0]), int(line[0].split('-')[1]), int(line[1].split('-')[0]),
                int(line[1].split('-')[1]))
            # part 1
            if contains(start1, end1, start2, end2) or contains(start2, end2, start1, end1):
                result_1 = result_1 + 1
            # part 2
            if overlaps(start1, end1, start2, end2) or overlaps(start2, end2, start1, end1):
                result_2 = result_2 + 1

        print(result_1)
        print(result_2)


def contains(x1, y1, x2, y2):
    return x1 <= x2 and y1 >= y2


def overlaps(x1, y1, x2, y2):
    return x1 in range(x2, y2 + 1) or y1 in range(x2, y2 + 1)


if __name__ == "__main__":
    day4()
