import numpy


class Monkey:

    def __init__(self, items, operation, test, true, false):
        self.items = [int(x.strip(",")) for x in items.split(" ")[4:]]
        self.operation = operation.split(" ")[6:]
        self.test = int(test.split(" ")[-1])
        self.true = int(true.split(" ")[-1])
        self.false = int(false.split(" ")[-1])
        self.num_inspections = 0


def day11():
    with open("./input11.txt", "r") as file:
        monkeys = []
        lines = [line.splitlines() for line in file.read().strip().split("\n\n")]

        for line in lines:
            monkeys.append(Monkey(line[1], line[2], line[3], line[4], line[5]))

        # part 1
        for _ in range(20):
            for monkey in monkeys:
                for item in monkey.items:
                    monkey.num_inspections += 1
                    operand = item if monkey.operation[1] == 'old' else int(monkey.operation[1])
                    if monkey.operation[0] == '*':
                        new = item * operand
                    else:
                        new = item + operand

                    new //= 3
                    if new % monkey.test == 0:
                        monkeys[monkey.true].items.append(new)
                    else:
                        monkeys[monkey.false].items.append(new)

                monkey.items = []

        monkey_business = [monkey.num_inspections for monkey in monkeys]
        monkey_business.sort(reverse=True)
        print(monkey_business[0] * monkey_business[1])

        # part 2
        monkeys_2 = []
        for line in lines:
            monkeys_2.append(Monkey(line[1], line[2], line[3], line[4], line[5]))

        test_vals = [monkey.test for monkey in monkeys_2]
        worry_reducer = 1
        for x in test_vals:
            worry_reducer *= x

        for _ in range(10000):
            for monkey in monkeys_2:
                for item in monkey.items:
                    monkey.num_inspections += 1
                    operand = item if monkey.operation[1] == 'old' else int(monkey.operation[1])
                    if monkey.operation[0] == '*':
                        new = item * operand
                    else:
                        new = item + operand

                    new %= worry_reducer
                    if new % monkey.test == 0:
                        monkeys_2[monkey.true].items.append(new)
                    else:
                        monkeys_2[monkey.false].items.append(new)

                monkey.items = []

        monkey_business_2 = [monkey.num_inspections for monkey in monkeys_2]
        monkey_business_2.sort(reverse=True)
        print(monkey_business_2[0] * monkey_business_2[1])


if __name__ == "__main__":
    day11()
