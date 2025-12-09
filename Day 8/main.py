import pathlib as pl
import math

def get_lines() -> list[tuple[int, int, int]]:
    content = []
    result: list[tuple[int, int, int]] = []
    # path = str(pl.Path(__file__).parent.resolve()) + "/data_tests.txt"
    path = str(pl.Path(__file__).parent.resolve()) + "/data.txt"
    with open(path, "r") as file:
        print(f"reading file contents of \"{path}\"")
        content = file.read()
    for line in content.split("\n"):
        x, y, z = line.split(",")
        result.append((int(x), int(y), int(z)))
    
    return result


def distance_between(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    ab = (a[0]-b[0], a[1]-b[1], a[2]-b[2])
    return math.sqrt(ab[0]**2 + ab[1]**2 + ab[2]**2)



def part_2():
    positions = get_lines()
    distances = []
    number_of_connections = 0

    print("calulating distances...")
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            distances.append(((i, j), distance_between(positions[i], positions[j])))

    circuits = [[i] for i in range(len(positions))]
    sorted_distances = sorted(distances, key=lambda x: x[1])

    x = 0
    while len(circuits) > 1:
        boxes, _ = sorted_distances[x]
        x += 1
        a, b = boxes
        a_found_at = -1 
        b_found_at = -1

        for i in range(len(circuits)):
            current_circuit = circuits[i]
            if a in current_circuit and b in current_circuit:
                a_found_at = b_found_at = i
            if a in current_circuit:
                a_found_at = i
            if b in current_circuit:
                b_found_at = i
            if a_found_at >= 0 and b_found_at >= 0:
                break
        
        if a_found_at == -1 and b_found_at == -1:
            circuits.append([a, b])
            number_of_connections += 1
        elif a_found_at == b_found_at:
            number_of_connections += 1
            continue
        elif a_found_at >= 0 and b_found_at == -1:
            circuits[a_found_at].append(b)
            number_of_connections += 1
        elif b_found_at >= 0 and a_found_at == -1:
            circuits[b_found_at].append(a)
            number_of_connections += 1
        elif a_found_at != b_found_at:
            circuits[a_found_at] += circuits[b_found_at]
            circuits.pop(b_found_at) 
            number_of_connections += 1

        if len(circuits) == 1:
            print(f"Result: {positions[a][0] * positions[b][0]}")    


def main():
    part_2()


if __name__ == "__main__":
    main()