from days.template.solution import Solution, read_input


class AlgorithmStep:
    count: int
    from_index: int
    to_index: int

    def __init__(self, count: int, from_index: int, to_index: int):
        self.count = count
        self.from_index = from_index
        self.to_index = to_index

    def __str__(self) -> str:
        return f'move {self.count} from {self.from_index} to {self.to_index}'


class Stack:
    values: list[str] = []

    def __init__(self):
        self.values = []

    def append(self, value):
        self.values.append(value)

    def pop(self) -> str:
        return self.values.pop()

    def pop_several(self, count: int) -> list[str]:
        ret = [self.values.pop() for i in range(0, count)]
        ret.reverse()
        return ret

    def __str__(self) -> str:
        return ', '.join(self.values)


def parse_stacks(stacks: list[str]) -> list[Stack]:
    rawlist = []

    i = 0
    current = stacks[i]
    while current != '' and i < len(stacks):
        rawlist.append(current)
        i += 1
        current = stacks[i]

    stacks_count = int(rawlist[-1][-1])
    rawlist.pop(-1)
    rawlist.reverse()

    ret = [Stack() for _ in range(0, stacks_count)]

    for line in rawlist:
        current_stack_index = 0
        while current_stack_index < stacks_count:
            if line == '':
                current_stack_index += 1
                break

            current_element = line[0:3][1]
            line = line[4:]

            if current_element != ' ':
                ret[current_stack_index].append(current_element)

            current_stack_index += 1


    # print('\n'.join([f'{e}' for e in stacks]))

    return ret


def parse_steps(steps: list[str]) -> list[AlgorithmStep]:
    steps = list(filter(lambda x: x.startswith('move'), steps))

    res = []
    for step in steps:
        digits = [int(s) for s in step.split() if s.isdigit()]
        res.append(AlgorithmStep(digits[0], digits[1], digits[2]))

    # print('\n'.join([f'{e}' for e in res]))

    return res

class SolutionDay05(Solution):
    stacks: list[Stack]
    steps: list[AlgorithmStep]

    def __init__(self, input: list[str]):
        self.stacks = parse_stacks(input)
        self.steps = parse_steps(input)

    def solve_first_part(self, input: list[str]) -> str:
        for step in self.steps:
            for i in range(step.count):
                self.stacks[step.to_index - 1].append(self.stacks[step.from_index - 1].pop())

        return ''.join([e.pop() for e in self.stacks])


    def solve_second_part(self, input: list[str]) -> str:
        for step in self.steps:
            for e in self.stacks[step.from_index - 1].pop_several(step.count):
                self.stacks[step.to_index - 1].append(e)

        return ''.join([e.pop() for e in self.stacks])

if __name__ == '__main__':
    input_lines = read_input()
    # print(input_lines)
    solution = SolutionDay05(input_lines)
    # print(solution.solve_first_part([]))
    print(solution.solve_second_part([]))
