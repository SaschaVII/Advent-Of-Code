import pathlib as pl


def get_lines() -> list[str]:
    content = []
    path = str(pl.Path(__file__).parent.resolve()) + "/data.txt"
    with open(path, "r") as file:
        print(f"reading file contents of \"{path}\"")
        content = file.read()
    return content.split("\n")


def split_data(data: list[str]) -> tuple[list[str], list[str]]:
    empty_line_index = 0
    for i in range(len(data)):
        if data[i] == "":
            empty_line_index = i
            break
    return (data[:empty_line_index], data[empty_line_index+1:])


def is_id_fresh(_id: int, ranges: list[str]) -> bool:
    for _range in ranges:
        middle = _range.find("-")
        lower = int(_range[:middle])
        upper = int(_range[middle+1:])
        if _id >= lower and _id <= upper:
            return True
    return False


def remove_zeros(ranges: list[tuple[int, int]]):
    occurrances = ranges.count((0, 0))
    for i in range(occurrances):
        ranges.remove((0, 0))
    return occurrances


# mashes ranges and returns a new copy of mashed ranges
def mash_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    first_run = True
    while remove_zeros(ranges) > 0 or first_run:
        first_run = False
        for i in range(len(ranges)):
            current = ranges[i]
            current_lower, current_upper = current

            for j in range(i + 1, len(ranges)):
                other_range = ranges[j]
                other_lower, other_upper = other_range
                # range fits entirely within another range appearing later
                if current_lower >= other_lower and current_upper <= other_upper:
                    ranges[i] = (0, 0)
                    break

                # lower intersection
                if current_lower <= other_lower and current_upper <= other_upper and current_upper <= other_lower:
                    ranges[j] = (current_lower, other_upper)
                    ranges[i] = (0, 0)
                    break
                    
                # upper intersection
                if current_lower >= other_lower and current_lower <= other_upper and current_upper >= other_upper:
                    ranges[j] = (other_lower, current_upper)
                    ranges[i] = (0, 0)
                    break
    return ranges
    
def count_ids_in_ranges(mashed_ranges: list[tuple[int, int]]) -> int:
    count = 0
    for mashed_range in mashed_ranges:
        count += mashed_range[1] - mashed_range[0] + 1
    return count

def main():
    count_1 = 0
    data = get_lines()
    ranges, ids = split_data(data)
    for _id in ids:
        if is_id_fresh(int(_id), ranges):
            count_1 += 1

    tupled_ranges = []
    for _range in ranges:
        middle = _range.find("-")
        tupled_ranges.append((int(_range[:middle]), int(_range[middle+1:])))

    count_2 = count_ids_in_ranges(mash_ranges(tupled_ranges))
    
    print("Part 1 Result:", count_1)
    print("Part 2 Result:", count_2)


if __name__ == "__main__":
    main()