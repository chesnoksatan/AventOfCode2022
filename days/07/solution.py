from enum import Enum

from days.template.solution import Solution, read_input


MAX_AMOUNT = 100000
SYSTEM_STORAGE_SIZE = 70000000
MUST_BE_AVAILABLE = 30000000


class EntityType(Enum):
    DIR = 0
    FILE = 1


class Entity:
    name: str
    size: int
    type: EntityType

    def __init__(self, name: str, type: EntityType, parent, size: int = 0):
        self.name = name
        self.type = type
        self.size = size
        self.parent = parent
        self.entity_list = []

    def append(self, entity) -> None:
        if self.type == EntityType.FILE: return
        self.entity_list.append(entity)

    def find(self, name: str) -> int:
        for i in range(len(self.entity_list)):
            if self.entity_list[i].name == name: return i
        return -1

    def calculate_size(self) -> int:
        if self.type == EntityType.FILE: return self.size
        if len(self.entity_list) == 0: return 0
        return sum([e.calculate_size() for e in self.entity_list])


class SolutionDay07(Solution):
    start_directory: Entity

    def __init__(self, input: list[str]):
        self.start_directory = Entity('/', EntityType.DIR, '')

        current_directory = self.start_directory
        for line in input[2:]:
            if line.startswith('dir'):
                current_directory.append(Entity(line[4:], EntityType.DIR, current_directory))
                continue
            elif line.startswith('$'):
                if line.find('cd') != -1:
                    arg = line[line.find('cd') + 3:]
                    if arg == '..':
                        current_directory = current_directory.parent
                    else:
                        current_directory = current_directory.entity_list[current_directory.find(arg)]
                    continue
            else:
                splitted = line.split(' ')
                current_directory.append(Entity(splitted[1], EntityType.FILE, current_directory, int(splitted[0])))
                continue

    def solve_first_part(self, input: list[str]) -> int:
        return calculate(self.start_directory)

    def solve_second_part(self, input: list[str]) -> int:
        total_size = self.start_directory.calculate_size()
        must_be_free = MUST_BE_AVAILABLE - (SYSTEM_STORAGE_SIZE - total_size)

        minimum = SYSTEM_STORAGE_SIZE
        for i in get_sizes_of_all_entities(self.start_directory):
            if must_be_free <= i < minimum:
                minimum = i

        return minimum


def calculate(entity: Entity) -> int:
    res = 0

    if entity.calculate_size() < MAX_AMOUNT: res += entity.calculate_size()
    for e in entity.entity_list:
        if e.type == EntityType.DIR:
            res += calculate(e)

    return res

# 1117448
def get_sizes_of_all_entities(entity: Entity) -> list[int]:
    sizes = []

    if entity.type == EntityType.DIR: sizes.append(entity.calculate_size())
    for e in entity.entity_list:
        if e.type == EntityType.DIR:
            sizes.extend(get_sizes_of_all_entities(e))

    return sizes


if __name__ == '__main__':
    input_lines = read_input()
    print(input_lines)
    solution = SolutionDay07(input_lines)
    print(solution.solve_first_part(input_lines))
    print(solution.solve_second_part(input_lines))
