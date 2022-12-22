def day8():
    with open("./input8.txt", "r") as file:
        lines = [[int(c) for c in line.strip()] for line in file.readlines()]

        # part 1
        num_visible_trees = (99 * 99) - (97 * 97)

        for i in range(1, 98):
            for j in range(1, 98):
                tree = lines[i][j]

                left_visible = True
                left = j - 1
                while left >= 0:
                    if lines[i][left] >= tree:
                        left_visible = False
                    left -= 1

                right_visible = True
                right = j + 1
                while right < 99:
                    if lines[i][right] >= tree:
                        right_visible = False
                    right += 1

                up_visible = True
                up = i - 1
                while up >= 0:
                    if lines[up][j] >= tree:
                        up_visible = False
                    up -= 1

                down_visible = True
                down = i + 1
                while down < 99:
                    if lines[down][j] >= tree:
                        down_visible = False
                    down += 1

                if any([left_visible, right_visible, up_visible, down_visible]):
                    num_visible_trees += 1

        print(num_visible_trees)

        # part 2
        scenic_scores = [0]
        for i in range(1, 98):
            for j in range(1, 98):
                tree = lines[i][j]

                left_score = 0
                left = j - 1
                while left >= 0:
                    left_score += 1
                    if lines[i][left] >= tree:
                        break
                    left -= 1

                if left_score == 0:
                    continue

                right_score = 0
                right = j + 1
                while right < 99:
                    right_score += 1
                    if lines[i][right] >= tree:
                        break
                    right += 1

                if right_score == 0:
                    continue

                up_score = 0
                up = i - 1
                while up >= 0:
                    up_score += 1
                    if lines[up][j] >= tree:
                        break
                    up -= 1

                if up_score == 0:
                    continue

                down_score = 0
                down = i + 1
                while down < 99:
                    down_score += 1
                    if lines[down][j] >= tree:
                        break
                    down += 1

                scenic_scores.append(left_score * right_score * up_score * down_score)

        print(max(scenic_scores))


if __name__ == "__main__":
    day8()
