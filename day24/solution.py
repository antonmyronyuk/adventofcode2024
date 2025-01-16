import itertools
import operator
from typing import NamedTuple

with open("input.txt") as input_file:
    initial_state_section, gates_section = input_file.read().strip().split("\n\n")

OPERATOR_TO_FUNCTION_MAP = {"AND": operator.and_, "OR": operator.or_, "XOR": operator.xor}
initial_wires = {}
operations = []
for row in initial_state_section.split("\n"):
    key, value = row.split(": ")
    initial_wires[key] = int(value)
for operation in gates_section.split("\n"):
    op1, operator, op2, _, res = operation.split(" ")
    operations.append((op1, op2, operator, res))


def process_calculation(initial_wires, operations):
    wires = initial_wires.copy()
    operations_applied = set()
    while len(operations_applied) < len(operations):
        changed = False
        for operation in operations:
            if operation in operations_applied:
                continue
            op1, op2, operator, res = operation
            if op1 in wires and op2 in wires:
                changed = True
                wires[res] = OPERATOR_TO_FUNCTION_MAP[operator](wires[op1], wires[op2])
                operations_applied.add(operation)

        if not changed:
            return None

    return wires


def get_wires_output_decimal(wires, prefix):
    bits = [value for key, value in sorted(wires.items()) if key.startswith(prefix)]
    return int("".join(map(str, reversed(bits))), 2)


def calc_tail_bin_distance(a, b):
    dist = 0
    while (1<<dist) & (a ^ b) == 0 and dist < 46:
        dist += 1

    return dist


class Node(NamedTuple):
    value: str
    operator: str | None = None
    left: "Node" = None
    right: "Node" = None


def draw_tree(node: Node | None, offset: int = 0):
    if not node:
        return

    draw_tree(node.left, offset + 1)
    print(" " * offset * 8, node.value, node.operator or "")
    draw_tree(node.right, offset + 1)


def get_gates(node: Node | None) -> list[str]:
    if not node:
        return []

    return [node.value, *get_gates(node.left), *get_gates(node.right)]


def get_gate_operations_tree(operations, gate):
    for operation in operations:
        op1, op2, operator, res = operation
        if res == gate:
            return Node(
                value=res,
                operator=operator,
                left=get_gate_operations_tree(operations, op1),
                right=get_gate_operations_tree(operations, op2),
            )

    return Node(value=gate)


def swap_operations(swap_pairs):
    for operation1, operation2 in swap_pairs:
        i1, i2 = operations.index(operation1), operations.index(operation2)
        operations[i1] = (*operation1[:3], operation2[3])
        operations[i2] = (*operation2[:3], operation1[3])


x = get_wires_output_decimal(initial_wires, "x")
y = get_wires_output_decimal(initial_wires, "y")
target_z = x + y
print(target_z, "target")

wires = process_calculation(initial_wires, operations)
actual_z = get_wires_output_decimal(wires, "z")
print(actual_z, "actual")  # part 1

print(bin(target_z), "target")
print(bin(actual_z), "actual")
print(bin(actual_z ^ target_z), "diff")
print(calc_tail_bin_distance(actual_z, target_z), "dist")

# draw_tree(get_gate_operations_tree(operations, "z08"))
# draw_tree(get_gate_operations_tree(operations, "z09"))

# draw_tree(get_gate_operations_tree(operations, "z16"))
# draw_tree(get_gate_operations_tree(operations, "z17"))

# draw_tree(get_gate_operations_tree(operations, "z28"))
# draw_tree(get_gate_operations_tree(operations, "z29"))

# draw_tree(get_gate_operations_tree(operations, "z39"))
# draw_tree(get_gate_operations_tree(operations, "z40"))

# detected using visual analysis of operations trees below
swaps = [
    (('kwv', 'ctv', 'OR', 'z08'), ('gvw', 'kgn', 'XOR', 'vvr')),
    (('y16', 'x16', 'AND', 'rnq'), ('y16', 'x16', 'XOR', 'bkr')),
    (('y28', 'x28', 'AND', 'z28'), ('djn', 'ptk', 'XOR', 'tfb')),
    (('thk', 'wnk', 'AND', 'z39'), ('wnk', 'thk', 'XOR', 'mqh')),
]
swap_operations(swaps)


wires = process_calculation(initial_wires, operations)
new_z = get_wires_output_decimal(wires, "z")
print()
print("after swap")
print(new_z, "new")
print(bin(new_z ^ target_z), "new diff")
print(calc_tail_bin_distance(new_z, target_z), "new dist")
outputs_to_swap = [swap[-1] for swap in itertools.chain.from_iterable(swaps)]
answer = ",".join(sorted(outputs_to_swap))
print(answer)  # part 2
