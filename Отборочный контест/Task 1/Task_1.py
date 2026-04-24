import sys


def read_ints(stream):
    return map(int, stream.readline().split())


def main():
    stream = sys.stdin
    n, queries_count = read_ints(stream)
    values = list(read_ints(stream))

    hits = [0] * (n + 2)
    for _ in range(queries_count):
        left, right = read_ints(stream)
        hits[left] += 1
        hits[right + 1] -= 1

    # running sum turns the +1/-1 markers into per-position hit counts
    for pos in range(1, n + 1):
        hits[pos] += hits[pos - 1]

    hit_counts = sorted(hits[1:n + 1], reverse=True)
    values.sort(reverse=True)

    answer = sum(value * count for value, count in zip(values, hit_counts))
    print(answer)


if __name__ == "__main__":
    main()
