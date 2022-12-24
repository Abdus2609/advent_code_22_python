def day10():
    with open("./input10.txt", "r") as file:
        lines = [line.strip().split(" ") for line in file.readlines()]

        cycle = 0
        reg_x = 1

        res_1 = 0
        for line in lines:
            if line[0] == "noop":
                cycle += 1
                res_1 += checkCycle(cycle, reg_x)
            elif line[0] == "addx":
                cycle += 1
                res_1 += checkCycle(cycle, reg_x)
                cycle += 1
                res_1 += checkCycle(cycle, reg_x)
                reg_x += int(line[1])

        print(res_1)

        # part 2
        crt = [['?' for _ in range(40)] for _ in range(6)]
        cycle_2 = 0
        reg_x_2 = 1

        for line in lines:
            if line[0] == "noop":
                cycle_2 += 1
                crt = update_crt(crt, cycle_2, reg_x_2)
            elif line[0] == "addx":
                cycle_2 += 1
                crt = update_crt(crt, cycle_2, reg_x_2)
                cycle_2 += 1
                crt = update_crt(crt, cycle_2, reg_x_2)
                reg_x_2 += int(line[1])

        for r in range(6):
            print(''.join(crt[r]))


def update_crt(crt, cycle, reg_x):
    prev_cycle = cycle - 1
    crt[prev_cycle // 40][prev_cycle % 40] = "#" if abs(reg_x - (prev_cycle % 40)) <= 1 else " "
    return crt


def checkCycle(cycle, reg_x):
    if cycle in [20, 60, 100, 140, 180, 220]:
        return cycle * reg_x
    else:
        return 0


if __name__ == "__main__":
    day10()
