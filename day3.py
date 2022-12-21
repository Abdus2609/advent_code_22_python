def day3():
    with open("./input3.txt", "r") as file:
        lines = [line.strip() for line in file.readlines()]

        # part 1
        result_1 = 0
        for line in lines:
            mid_index = int(len(line) / 2)
            (left_str, right_str) = (line[:mid_index], line[mid_index:])
            for c in left_str:
                if c in right_str:
                    result_1 = result_1 + priority(c) + 1
                    break

        print(result_1)

        # part 2
        result_2 = 0
        for i in range(0, len(lines), 3):
            for c in lines[i]:
                if c in lines[i + 1] and c in lines[i + 2]:
                    result_2 = result_2 + priority(c) + 1
                    break

        print(result_2)


def priority(item):
    if item.isupper():
        return (ord(item) - ord("A")) + 26
    else:
        return ord(item) - ord("a")


if __name__ == "__main__":
    day3()
