
def maxCal():
    calories = []

    with open("./day1input1.txt", "r") as file:
        lines = [line.strip() for line in file.readlines()]
        lines.append('')

        curr = 0
        for line in lines:
            if not line:
                calories.append(curr)
                curr = 0
            else:
                curr = curr + int(line)

    # part 1
    print(max(calories))

    # part 2
    calories.sort(reverse=True)
    print(calories[0] + calories[1] + calories[2])


if __name__ == "__main__":
    maxCal()
