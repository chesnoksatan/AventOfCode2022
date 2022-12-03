from days.template.solution import Solution


class SolutionDay01(Solution):
    def solve_first_part(self, input: list[int]) -> int:
        input.sort()
        return input[-1]

    def solve_second_part(self, input: list[int]) -> int:
        input.sort()
        return sum(input[-3:])

def read_input() -> list[int]:
    input_file_name = 'input.txt'
    try:
        elf_calories = []
        with open(input_file_name) as file:
            cal = 0
            for line in file.readlines():
                if line == '\n':
                    elf_calories.append(cal)
                    cal = 0
                else:
                    cal += int(line)
        return elf_calories
    except EnvironmentError:
        raise Exception(f"File {input_file_name} is missing or invalid")

if __name__ == '__main__':
    input_lines = read_input()
    solution = SolutionDay01()
    print(solution.solve_first_part(input_lines))
    print(solution.solve_second_part(input_lines))
