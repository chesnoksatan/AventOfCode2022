import string

from days.template.solution import Solution, read_input


values = {c: string.ascii_lowercase.index(c) + 1 for c in string.ascii_lowercase}
values.update({c: string.ascii_uppercase.index(c) + 1 + 26 for c in string.ascii_uppercase})


class SolutionDay03(Solution):
    def solve_first_part(self, input: list[str]) -> int:
        pairs = [(line[:len(line) // 2], line[len(line) // 2:]) for line in input]
        chars = []
        for pair in pairs:
            for char_i in pair[0]:
                index = pair[1].find(char_i)
                if index != -1:
                    chars.append(char_i)
                    break

        return sum([values[c] for c in chars])

    def solve_second_part(self, input: list[str]) -> int:
        groups = [ (input[i], input[i + 1], input[i + 2]) for i in range(0, len(input), 3) ]

        chars = []
        for triple in groups:
            for char_i in triple[0]:
                index_1 = triple[1].find(char_i)
                index_2 = triple[2].find(char_i)
                if index_1 != -1 and index_2 != -1:
                    chars.append(char_i)
                    break

        return sum([values[c] for c in chars])

if __name__ == '__main__':
    input_lines = read_input()
    solution = SolutionDay03()
    print(solution.solve_first_part(input_lines))
    print(solution.solve_second_part(input_lines))
