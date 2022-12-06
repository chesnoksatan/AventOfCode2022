from days.template.solution import Solution


class SolutionDay06(Solution):
    def solve_first_part(self, input: str) -> int:
        marker_length = 4
        i = 0
        while True and i < len(input) - marker_length:
            d = {}
            for ch in input[i : i + marker_length ]:
                d.setdefault(ch, 0)
                d[ch] += 1

            if len(d.keys()) == marker_length: break
            i += 1

        return i + marker_length

    def solve_second_part(self, input: str) -> int:
        marker_length = 14
        i = 0
        while True and i < len(input) - marker_length:
            d = {}
            for ch in input[i: i + marker_length]:
                d.setdefault(ch, 0)
                d[ch] += 1

            if len(d.keys()) == marker_length: break
            i += 1

        return i + marker_length


def read_input() -> str:
    input_file_name = 'input.txt'
    try:
        with open(input_file_name) as file:
            return file.readline()
    except EnvironmentError:
        raise Exception(f"File {input_file_name} is missing or invalid")

if __name__ == '__main__':
    input_lines = read_input()
    print(input_lines)
    solution = SolutionDay06()
    print(solution.solve_first_part(input_lines))
    print(solution.solve_second_part(input_lines))
