import pathlib as pl

def get_graph() -> dict[str, list[str]]:
    content = []
    result: dict[str, list[str]] = {}
    # path = str(pl.Path(__file__).parent.resolve()) + "/data_tests.txt"
    path = str(pl.Path(__file__).parent.resolve()) + "/data.txt"

    with open(path, "r") as file:
        print(f"reading file contents of \"{path}\"")
        content = file.read()

    for line in content.split("\n"):
        name = line[:line.find(":")]
        outputs = line[line.find(":")+2:].split()
        result[name] = outputs
    
    return result


def ways_to_end(name: str, graph: dict[str, list[str]]) -> int:   
    if "out" in graph[name]:
        return 1
    
    count = 0
    for output in graph[name]:
        count += ways_to_end(output, graph)

    return count


def part_1():
    graph = get_graph()

    result = ways_to_end("you", graph)

    print(f"Result part 1: {result}")
        



def main():
    part_1()

if __name__ == "__main__":
    main()