def day13():
    with open("./input13.txt", "r") as file:
        result_1 = 0
        packets = []
        # part 1
        for i, group in enumerate(file.read().strip().split("\n\n")):
            fst, snd = group.split("\n")
            fst = eval(fst)
            snd = eval(snd)
            packets.extend([fst, snd])
            if compare(fst, snd) == -1:
                result_1 += i + 1

        print(result_1)

        # part 2
        packets.extend([[[2]], [[6]]])
        from functools import cmp_to_key
        packets = sorted(packets, key=cmp_to_key(compare))
        result_2 = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)
        print(result_2)


def compare(list1, list2):
    if isinstance(list1, int) and isinstance(list2, int):
        return -1 if list1 < list2 else (0 if list1 == list2 else 1)
    elif isinstance(list1, int) and isinstance(list2, list):
        return compare([list1], list2)
    elif isinstance(list1, list) and isinstance(list2, int):
        return compare(list1, [list2])
    elif isinstance(list1, list) and isinstance(list2, list):
        i = 0
        while i < len(list1) and i < len(list2):
            res = compare(list1[i], list2[i])
            if res != 0:
                return res
            i += 1
        if i == len(list1) and i < len(list2):
            return -1
        elif i == len(list2) and i < len(list1):
            return 1
        else:
            return 0


if __name__ == "__main__":
    day13()
