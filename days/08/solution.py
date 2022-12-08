from days.template.solution import Solution, read_input


class Tree:
    height: int
    visible: bool

    def __init__(self, height: int, visible: bool = False):
        self.height = height
        self.visible = visible

    def __str__(self):
        return f'Height: {self.height}, Visible: {self.visible}'

    def __gt__(self, other):
        return self.height > other.height

    def __lt__(self, other):
        return self.height < other.height

    def __eq__(self, other):
        return self.height == other.height


class SolutionDay08(Solution):
    forest: list[list[Tree]]

    def __init__(self, input: list[str]):
        self.forest = [[Tree(int(ch)) for ch in line]for line in input]

    #1825
    def solve_first_part(self, input: list[str]) -> int:
        total_visible_trees = 2 * (len(self.forest) + len(self.forest[0]) - 2)

        for i in range(1, len(self.forest) - 1):
            for j in range(1, len(self.forest[i]) - 1):
                current_tree = self.forest[i][j]

                if all([current_tree > tree and not current_tree.visible for tree in self.forest[i][0:j]]):
                    total_visible_trees += 1
                    current_tree.visible = True
                elif all([current_tree > tree and not current_tree.visible for tree in self.forest[i][j + 1:]]):
                    total_visible_trees += 1
                    current_tree.visible = True
                elif all([current_tree > self.forest[k][j] and not current_tree.visible for k in range(0, i)]):
                    total_visible_trees += 1
                    current_tree.visible = True
                elif all([current_tree > self.forest[k][j] and not current_tree.visible for k in range(i + 1, len(self.forest))]):
                    total_visible_trees += 1
                    current_tree.visible = True


        return total_visible_trees

# FUUUUUUUUUUUCK
    def solve_second_part(self, input: list[str]) -> int:

        row_len = len(self.forest)
        col_len = len(self.forest[0])

        scores_table = [[0 for _ in range(col_len)] for _ in range(row_len)]

        def calculate_score(left: int, right: int, top: int, bottom: int) -> int:
            return left * right * top * bottom

        high_score = 0
        for i in range(1, row_len - 1):
            for j in range(1, col_len - 1):
                pass

        return high_score


if __name__ == '__main__':
    input_lines = read_input()
    print(input_lines)
    solution = SolutionDay08(input_lines)
    print(solution.solve_first_part(input_lines))
    print(solution.solve_second_part(input_lines))
