# Advent of Code 2024 — Day 2: Red-Nosed Reports

Solution to [Day 2](https://adventofcode.com/2024/day/2).

A report is a line of space-separated levels. It's **safe** when:
- the levels are all increasing or all decreasing, and
- every adjacent pair differs by between 1 and 3.

- **Part 1** — count the safe reports.
- **Part 2** — same, but a report also counts as safe if removing a single level makes it safe (the "Problem Dampener").

## Run

```bash
python3 day2.py
```

The program reads from `input.txt`. The included `input.txt` is the example from the
puzzle (expected output: Part 1 = 2, Part 2 = 4). Replace it with your own puzzle
input to get your answers.
