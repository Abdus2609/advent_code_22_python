scores_1 = {"X": 1, "Y": 2, "Z": 3}
strategy_1 = {"A": "Y", "B": "Z", "C": "X"}
mapping = {"A": "X", "B": "Y", "C": "Z"}


def day2():
    with open("./input2.txt", "r") as file:
        games = [line.strip().split(" ") for line in file.readlines()]
        print(games)

        # part 1
        score_1 = 0
        for game in games:
            their_move = game[0]
            my_move = game[1]
            score_1 = score_1 + scores_1[my_move]
            result = 0
            if my_move == strategy_1[their_move]:
                result = 6
            elif my_move == mapping[their_move]:
                result = 3

            score_1 = score_1 + result

        print(score_1)

        # part 2
        score_2 = 0
        for game in games:
            their_move = game[0]
            my_move = game[1]

            if my_move == "X":
                move_score = scores_1[mapping[their_move]] - 1
                if move_score == 0:
                    move_score = 3
                score_2 = score_2 + move_score
            elif my_move == "Y":
                move_score = scores_1[mapping[their_move]]
                score_2 = score_2 + move_score + 3
            else:
                move_score = scores_1[mapping[their_move]] + 1
                if move_score == 4:
                    move_score = 1
                score_2 = score_2 + move_score + 6

        print(score_2)


if __name__ == "__main__":
    day2()
