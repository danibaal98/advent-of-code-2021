from __future__ import annotations
from typing import NamedTuple, Tuple

class Board(NamedTuple):
    left: set[int]
    ints: list[list[int]]

    @property
    def has_won(self) -> bool:
        for i in range(5):
            for j in range(5):
                if self.ints[i][j] in self.left:
                    break
            else:
                return True

            for j in range(5):
                if self.ints[j][i] in self.left:
                    break
            else:
                return True
        else:
            return False
        

    @classmethod
    def parse(cls, board: str) -> Board:
        board_row = []
        ints = []
        left = set()

        for row in board.split("\n"):
            if row == "":
                continue
            board_row = [int(x) for x in row.split()]
            ints.append(board_row)
            left.update(board_row)

        return cls(left, ints)

def problem1() -> int:
    movements, boards = get_data()
    for number in movements:
        for board in boards:
            board.left.discard(number)

        for board in boards:
            if board.has_won:
                return sum(board.left) * number

def problem2() -> int:
    movements, boards = get_data()

    last_winner = -1
    seen = set()

    for number in movements:
        for board in boards:
            board.left.discard(number)

        for i, board in enumerate(boards):
            if i not in seen and board.has_won:
                last_winner = sum(board.left) * number
                seen.add(i)

    return last_winner

def get_data() -> Tuple[list[int], list[Board]]:
    with open("../data.txt", "r") as f:
        data_input = f.read()

    first, *rest = data_input.split("\n\n")

    boards = [Board.parse(board) for board in rest]

    movements = [int(x) for x in first.split(",")]
    return movements, boards

if __name__ == "__main__":
    solution1 = problem1()
    solution2 = problem2()
    print(solution1)
    print(solution2)

