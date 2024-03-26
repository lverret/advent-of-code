import argparse


def read_txt(filename):
    return open(filename, 'r').read().splitlines()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="General runner for AoC")
    parser.add_argument("days", help="AoC list of days", nargs="+")
    args = parser.parse_args()
    for day in args.days:
        lines = read_txt(f"inputs/{day}.txt")
        part1 = getattr(__import__(day), "part1", None)
        part2 = getattr(__import__(day), "part2", None)
        if part1 is not None:
            print(part1(lines.copy()))
        if part2 is not None:
            print(part2(lines.copy()))
