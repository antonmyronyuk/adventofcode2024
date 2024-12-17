def get_combo_operand_value(operand, a, b, c):
    if operand < 4:
        return operand
    if operand == 4:
        return a
    if operand == 5:
        return b
    if operand == 6:
        return c


def run_program(program, a, b, c, part2=False):
    out = []
    i = 0
    while i < len(program):
        op = program[i]
        operand = program[i + 1]
        combo_operand = get_combo_operand_value(operand, a, b, c)
        match op:
            case 0:
                a = a >> combo_operand
            case 1:
                b = b ^ operand
            case 2:
                b = combo_operand & 7
            case 3 if a != 0:
                i = operand
                continue
            case 4:
                b = b ^ c
            case 5:
                out.append(combo_operand & 7)
                if part2 and out[len(out) - 1] != program[len(out) - 1]:
                    return out
            case 6:
                b = a >> combo_operand
            case 7:
                c = a >> combo_operand

        i += 2

    return out


def find_minimal_a(program):
    n = len(program) // 2 + 1
    div = 8**n
    # mod = 192  # for the example
    mod = 61442458  # brute forced, checked the command beginning is the same
    mul = 1
    while True:
        a = mul * div + mod
        if run_program(program, a, 0, 0) == program:
            return a
        mul += 1


program = [2,4,1,5,7,5,4,3,1,6,0,3,5,5,3,0]
print(run_program(program, 61156655, 0, 0))  # part 1
print(find_minimal_a(program))  # part 2
