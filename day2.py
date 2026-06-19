def safe(levels):
    diffs = [b - a for a, b in zip(levels, levels[1:])]
    increasing = all(d > 0 for d in diffs)
    decreasing = all(d < 0 for d in diffs)
    in_range = all(1 <= abs(d) <= 3 for d in diffs)
    return (increasing or decreasing) and in_range


def safe_with_dampener(levels):
    if safe(levels):
        return True
    for i in range(len(levels)):
        if safe(levels[:i] + levels[i + 1:]):
            return True
    return False


def main():
    with open("input.txt") as f:
        reports = [[int(n) for n in line.split()] for line in f if line.strip()]

    part1 = sum(1 for r in reports if safe(r))
    part2 = sum(1 for r in reports if safe_with_dampener(r))

    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == "__main__":
    main()
