def day7():
    with open("./input7.txt", "r") as file:
        lines = [line.strip().split(" ") for line in file.readlines()]

        path = '/home'
        dirs = {'/home': 0}

        for line in lines:

            if line[0] == '$':
                if line[1] == 'ls':
                    pass
                elif line[1] == 'cd':
                    if line[2] == '/':
                        path = '/home'
                    elif line[2] == '..':
                        path = path[:path.rfind('/')]
                    else:
                        dir_name = line[2]
                        path = path + '/' + dir_name
                        dirs.update({path: 0})
            elif line[0] == 'dir':
                pass
            else:
                size = int(line[0])
                curr_dir = path
                for i in range(path.count('/')):
                    dirs[curr_dir] += size
                    curr_dir = curr_dir[:curr_dir.rfind('/')]

        # part 1
        result_1 = 0
        for curr_dir in dirs:
            if dirs[curr_dir] <= 100000:
                result_1 += dirs[curr_dir]

        print(result_1)

        # part 2
        space_needed = 30000000 - (70000000 - dirs['/home'])
        valid_dirs = []

        for curr_dir in dirs:
            if space_needed <= dirs[curr_dir]:
                valid_dirs.append(dirs[curr_dir])

        result_2 = min(valid_dirs)
        print(result_2)


if __name__ == "__main__":
    day7()
