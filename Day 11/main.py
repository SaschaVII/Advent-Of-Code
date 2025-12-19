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

memo = {} # memo needs to include the fft and dac states
def ways_to_end_2(name: str, graph: dict[str, list[str]], fft: bool = False, dac: bool = False) -> int:
    key = f"{name} {fft} {dac}"
    if key in memo.keys():
        return memo[key]

    fft = True if name == "fft" else fft
    dac = True if name == "dac" else dac
    
    if "out" in graph[name]:
        if (fft and dac):
            memo[key] = 1
            return 1
        memo[key] = 0
        return 0
    
    count = 0
    for output in graph[name]:
        count += ways_to_end_2(output, graph, fft, dac)

    memo[key] = count
    return count


def part_1():
    graph = get_graph()

    result = ways_to_end("you", graph)

    print(f"Result part 1: {result}")
        
# all paths that go from "svr" through "fft" and "dac" then "out"
def part_2():
    graph = get_graph()
    result = ways_to_end_2("svr", graph)

    print(f"Result part 2: {result}")


def main():
    part_2()

if __name__ == "__main__":
    main()