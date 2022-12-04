from days.template.solution import Solution, read_input

class Elf:
    start_section: int
    end_section: int

    def __init__(self, elf_range: str):
        self.start_section, self.end_section = (int(e) for e in elf_range.split('-'))

    def __str__(self) -> str:
        return f'From {self.start_section} to {self.end_section}'


def contains(first: Elf, second: Elf) -> bool:
    return (first.start_section >= second.start_section and first.end_section <= second.end_section) or\
        (second.start_section >= first.start_section and second.end_section <= first.end_section)

def overlaps(first: Elf, second: Elf) -> bool:
    return  first.start_section <= second.start_section <= first.end_section or \
        second.start_section <= first.start_section <= second.end_section


class SolutionDay04(Solution):
    elves_pairs: list[tuple[Elf, Elf]] = []

    def __init__(self, input: list[str]):
        self.elves_pairs = [(Elf(pair.split(',')[0]), Elf(pair.split(',')[1])) for pair in input]

    def solve_first_part(self, input: list[str]) -> int:
        return sum([contains(pair[0], pair[1]) for pair in self.elves_pairs])

    def solve_second_part(self, input: list[str]) -> int:
        return sum([overlaps(pair[0], pair[1]) for pair in self.elves_pairs])

if __name__ == '__main__':
    input_lines = read_input()
    solution = SolutionDay04(input_lines)
    print(solution.solve_first_part(input_lines))
    print(solution.solve_second_part(input_lines))
