import pathlib as pl


def get_lines() -> list[tuple[int, int]]:
    content = []
    result: list[tuple[int, int]] = []
    # path = str(pl.Path(__file__).parent.resolve()) + "/data_tests.txt"
    path = str(pl.Path(__file__).parent.resolve()) + "/data.txt"
    with open(path, "r") as file:
        print(f"reading file contents of \"{path}\"")
        content = file.read()
    for line in content.split("\n"):
        x, y = line.split(",")
        result.append((int(x), int(y)))
    
    return result


def rectangle_size(a: tuple[int, int], b: tuple[int, int]) -> int:
    return (abs(a[0]-b[0])+1)*(abs(a[1]-b[1])+1)


def part_1():
    red_tiles = get_lines()
    largest = 0
    for i in range(len(red_tiles)):
        for j in range(i+1, len(red_tiles)):
            largest = max(rectangle_size(red_tiles[i], red_tiles[j]), largest)

    print(f"result: ", largest)


# shrunk version of rectangle that is offlimit
def get_offlimit_points(a: tuple[int, int], c: tuple[int, int]) -> set[tuple[int, int]]:
    # technically doesn't work for recangles with a height or width of 1, but can't imagine the result is one of those anyways!!!
    result: set[tuple[int, int]] = set()    
    incr_x = 1 if a[0] < c[0] else -1
    for x in range(a[0] + incr_x, c[0], incr_x):
        incr_y = 1 if a[1] < c[1] else -1
        for y in range(a[1] + incr_y, c[1], incr_y):
            result.add((x, y))
    return result


def valid_rectangle(a: tuple[int, int], c: tuple[int, int], points: list[tuple[int, int]]) -> bool:
    offlimit_points = get_offlimit_points(a, c)
    for point in points:
        if point in offlimit_points:
            return False
    return True


def FUCK():
    points = get_lines()
    largest = 0

    for i in range(len(points)):
            print(f"checking row {i}")
            for j in range(i+1, len(points)):
                print(f"checking col {j}")
                current_size = rectangle_size(points[i], points[j])
                if current_size > largest and valid_rectangle(points[i], points[j], points):
                    rect_valid = True
                    print(f"new largest rectangle found: {points[i]} {points[j]} size {current_size}")
                    largest = current_size
    print(largest)
        

def main():
    # part_1()
    # part_2()
    # fuck_my_life()
    FUCK()

if __name__ == "__main__":
    main()