import pathlib as pl

def get_lines() -> list[str]:
    content = []
    path = str(pl.Path(__file__).parent.resolve()) + "/data.txt"
    with open(path, "r") as file:
        print(f"reading file contents of \"{path}\"")
        content = file.read()
    return content.split("\n")

def main():
    grid = get_lines()
    count = 0
    removed_at_least_one_roll = True

    while removed_at_least_one_roll:
        removed_at_least_one_roll = False
        for row_index in range(len(grid)):
            for col_index in range(len(grid[row_index])):
                if grid[row_index][col_index] != "@":
                    continue
                adjacent_rolls = 0
                is_first_col = True if col_index == 0 else False
                is_last_col = True if col_index == len(grid[row_index])-1 else False
                start = col_index if is_first_col else col_index-1
                end = col_index+1 if is_last_col else col_index+2
                
                if row_index-1 >= 0:
                    adjacent_rolls += grid[row_index-1][start:end].count("@")

                adjacent_rolls += grid[row_index][start:end].count("@")-1

                if row_index+1 < len(grid):
                    adjacent_rolls += grid[row_index+1][start:end].count("@")
                
                if adjacent_rolls < 4:
                    removed_at_least_one_roll = True
                    lst = list(grid[row_index])
                    lst[col_index] = "."
                    grid[row_index] = "".join(lst)
                    count += 1

    print("Result:", count)

if __name__ == "__main__":
    main()