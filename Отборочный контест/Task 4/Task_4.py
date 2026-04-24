import sys
from collections import defaultdict


def solve():
    tokens = sys.stdin.buffer.read().split()
    pos = 0

    def next_int():
        nonlocal pos
        val = int(tokens[pos])
        pos += 1
        return val

    epochs = next_int()
    per_epoch = next_int()

    entries = []
    for epoch in range(epochs):
        for _ in range(per_epoch):
            entries.append((next_int(), epoch))

    entries.sort()
    total_entries = len(entries)

    seen_in_window = defaultdict(int)
    distinct_epochs_covered = 0
    tightest_span = float('inf')
    tightest_windows = []

    left = 0
    for right in range(total_entries):
        _, epoch = entries[right]
        if seen_in_window[epoch] == 0:
            distinct_epochs_covered += 1
        seen_in_window[epoch] += 1

        while distinct_epochs_covered == epochs:
            span = entries[right][0] - entries[left][0]
            if span < tightest_span:
                tightest_span = span
                tightest_windows = [(left, right)]
            elif span == tightest_span:
                tightest_windows.append((left, right))

            left_epoch = entries[left][1]
            seen_in_window[left_epoch] -= 1
            if seen_in_window[left_epoch] == 0:
                distinct_epochs_covered -= 1
            left += 1

    best_sum = float('inf')
    best_pick = None

    for lo, hi in tightest_windows:
        pick = {}
        for k in range(lo, hi + 1):
            value, epoch = entries[k]
            if epoch not in pick:
                pick[epoch] = value
        candidate_sum = sum(pick.values())
        if candidate_sum < best_sum:
            best_sum = candidate_sum
            best_pick = sorted(pick.values())

    print(' '.join(map(str, best_pick)))


if __name__ == "__main__":
    solve()
