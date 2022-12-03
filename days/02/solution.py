from enum import Enum

from days.template.solution import Solution, read_input

class GameResult(Enum):
    WIN = 6
    DRAW = 3
    LOST = 0

plays = {
    ('A', 'X'): GameResult.DRAW,
    ('B', 'Y'): GameResult.DRAW,
    ('C', 'Z'): GameResult.DRAW,
    ('A', 'Y'): GameResult.WIN,
    ('B', 'Z'): GameResult.WIN,
    ('C', 'X'): GameResult.WIN,
    ('A', 'Z'): GameResult.LOST,
    ('B', 'X'): GameResult.LOST,
    ('C', 'Y'): GameResult.LOST,
}

cheat = {
    'X': GameResult.LOST,
    'Y': GameResult.DRAW,
    'Z': GameResult.WIN
}

shapes = { 'X': 1, 'Y': 2, 'Z': 3 }

def score_by_shape(shape: str) -> int:
    return shapes[shape]


def calculate(first: str, second: str) -> int:
    return plays[(first, second)].value + score_by_shape(second)


class SolutionDay02:
    def solve_first_part(self, input: list[str]) -> int:
        return sum([calculate(round.split(' ')[0], round.split(' ')[1]) for round in input])

    def solve_second_part(self, input: list[str]) -> int:

        def use_cheat(first_shape: str, second_shape: str) -> str:
            for k, v in plays.items():
                if cheat[second_shape] is v:
                    if first_shape == k[0]:
                        return k[1]

        results = []
        for round in input:
            first_shape = round.split(' ')[0]
            second_shape = round.split(' ')[1]
            results.append(calculate(first_shape, use_cheat(first_shape, second_shape)))

        return sum(results)


if __name__ == '__main__':
    input_lines = read_input()
    solution = SolutionDay02()
    print(solution.solve_first_part(input_lines))
    print(solution.solve_second_part(input_lines))
