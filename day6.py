def day6():
    with open("./input6.txt", "r") as file:
        line = file.readline().strip()

        result_1 = 0

        for i in range(len(line) - 4):
            visited = set()
            visited.add(line[i])
            visited.add(line[i + 1])
            visited.add(line[i + 2])
            visited.add(line[i + 3])
            if len(visited) == 4:
                result_1 = i + 4
                break

        # part 1
        print(result_1)

        result_2 = 0
        for i in range(len(line) - 14):
            visited = set()
            visited.add(line[i])
            visited.add(line[i + 1])
            visited.add(line[i + 2])
            visited.add(line[i + 3])
            visited.add(line[i + 4])
            visited.add(line[i + 5])
            visited.add(line[i + 6])
            visited.add(line[i + 7])
            visited.add(line[i + 8])
            visited.add(line[i + 9])
            visited.add(line[i + 10])
            visited.add(line[i + 11])
            visited.add(line[i + 12])
            visited.add(line[i + 13])
            if len(visited) == 14:
                result_2 = i + 14
                break

        print(result_2)


if __name__ == "__main__":
    day6()
