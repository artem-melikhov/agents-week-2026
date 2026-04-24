import sys


def solve():
    tokens = sys.stdin.buffer.read().split()
    pos = 0

    def next_int():
        nonlocal pos
        val = int(tokens[pos])
        pos += 1
        return val

    length = next_int()
    safe_count = next_int()

    is_safe = bytearray(length + 1)
    is_safe[0] = 1
    is_safe[length] = 1
    for _ in range(safe_count):
        spot = next_int()
        is_safe[spot] = 1

    unreachable = length + 2

    # forward pass: fewest jumps to reach each safe cell from the start
    steps_from_start = [unreachable] * (length + 1)
    steps_from_start[0] = 0
    for cell in range(length + 1):
        current = steps_from_start[cell]
        if current >= unreachable:
            continue
        for hop in (1, 2):
            target = cell + hop
            if target <= length and is_safe[target] and steps_from_start[target] > current + 1:
                steps_from_start[target] = current + 1

    if steps_from_start[length] >= unreachable:
        print(-1)
        return

    print(steps_from_start[length])

    # backward pass: fewest jumps from each safe cell to the finish
    steps_to_end = [unreachable] * (length + 1)
    steps_to_end[length] = 0
    for cell in range(length - 1, -1, -1):
        if cell != 0 and not is_safe[cell]:
            continue
        for hop in (1, 2):
            target = cell + hop
            if target <= length and is_safe[target] and steps_to_end[target] < unreachable:
                candidate = steps_to_end[target] + 1
                if candidate < steps_to_end[cell]:
                    steps_to_end[cell] = candidate

    best_total = steps_from_start[length]
    moves = []
    cursor = 0
    while cursor < length:
        one_hop = cursor + 1
        if (one_hop <= length and is_safe[one_hop]
                and steps_from_start[cursor] + 1 + steps_to_end[one_hop] == best_total):
            moves.append('1')
            cursor = one_hop
        else:
            moves.append('2')
            cursor += 2

    sys.stdout.write(''.join(moves) + '\n')


if __name__ == "__main__":
    solve()
