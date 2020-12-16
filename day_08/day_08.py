with open("input.txt", "r") as data_input:
    # import lines as an array eg. ['nop +0', 'acc +1', 'jmp +4', 'acc +3', 'jmp -3', 'acc -99', 'acc +1', 'jmp -4', 'acc +6']
    instructions = [line.rstrip() for line in data_input]


def part1(instructions):
    acc_value = 0
    next_instruction = 0
    performed_instructions = []
    infinite_loop = False

    while True:

        operation, argument = instructions[next_instruction].split(" ")

        if len(instructions) - 1 == next_instruction:
            infinite_loop = True

        if operation == "nop":
            next_instruction += 1
        if operation == "acc":
            acc_value += int(argument)
            next_instruction += 1
        if operation == "jmp":
            next_instruction += int(argument)

        if next_instruction in performed_instructions:
            infinite_loop = False
            return (f" Program entered an infinite loop. Acc value prior infinite loop is: {acc_value}", infinite_loop)

        if infinite_loop:
            return (f" Program ended successfully. It's acc value is: {acc_value}", infinite_loop)
        performed_instructions.append(next_instruction)


def part2(instruction):
    for i in range(1, len(instructions)):
        temp = instruction[:]

        operation, argument = temp[i].split(" ")

        if operation == "nop":
            operation = "jmp"
        elif operation == "jmp":
            operation = "nop"

        temp[i] = operation + " " + argument

        result = part1(temp)
        if result[1]:
            return result[0]
    return False


print(f"Part 1 | {part1(instructions)[0]}")
print(f"Part 2 | {part2(instructions)}")
