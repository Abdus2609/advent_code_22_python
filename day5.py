def day5():
    with open("./input5.txt", "r") as file:
        stack_strings, instructions = (line.splitlines() for line in file.read().strip("\n").split("\n\n"))
        stack_strings = [string.replace('    ', ' ').split(' ') for string in stack_strings]
        stack_strings.pop()
        stacks = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

        for row in stack_strings:
            for i in range(9):
                if len(row[i]) != 0:
                    letter = row[i].replace('[', '').replace(']', '')
                    stacks[i + 1].insert(0, letter)

        instructions = [instr.replace('move ', '').replace('from ', '').replace('to ', '').split(' ') for instr in
                        instructions]

        # part 1
        for instr in instructions:
            quantity = int(instr[0])
            src = int(instr[1])
            dst = int(instr[2])

            for i in range(quantity):
                crate = stacks[src].pop()
                stacks[dst].append(crate)

        result_1 = ''
        for stack in stacks.values():
            result_1 = result_1 + stack[-1]

        print(result_1)

        # part 2
        stacks_2 = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
        for row in stack_strings:
            for i in range(9):
                if len(row[i]) != 0:
                    letter = row[i].replace('[', '').replace(']', '')
                    stacks_2[i + 1].insert(0, letter)

        for instr in instructions:
            quantity = int(instr[0])
            src = int(instr[1])
            dst = int(instr[2])

            tmp = []
            for i in range(quantity):
                crate = stacks_2[src].pop()
                tmp.insert(0, crate)

            stacks_2[dst].extend(tmp)

        result_2 = ''
        for stack in stacks_2.values():
            result_2 = result_2 + stack[-1]

        print(result_2)


if __name__ == "__main__":
    day5()
