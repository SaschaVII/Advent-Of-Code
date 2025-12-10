import pathlib as pl

# returns a list of machines tuples
def get_machines() -> list[tuple[str, list[set[int]], list[int]]]:
    content = []
    result: list[tuple[str, list[set[int]], list[int]]] = []
    # path = str(pl.Path(__file__).parent.resolve()) + "/data_tests.txt"
    path = str(pl.Path(__file__).parent.resolve()) + "/data.txt"

    with open(path, "r") as file:
        print(f"reading file contents of \"{path}\"")
        content = file.read()

    for line in content.split("\n"):
        end_lights = line.find("]") + 1
        start_joltages = line.find("{")

        lights = line[1:end_lights-1]
        buttons_str = [x[1:-1].split(",") for x in line[end_lights+1:start_joltages-1].split(" ")]
        buttons: list[set[int]] = []
        for button in buttons_str:
            buttons.append(set([int(num) for num in button]))
        joltages = [int(x) for x in line[start_joltages+1:-1].split(",")]
        result.append((lights, buttons, joltages))
    
    return result
        

def apply_button(lights: str, button: set[int]) -> str:
    result = ""
    for i in range(len(lights)):
        if i not in button: result+= lights[i]
        else: result += "." if lights[i] == "#" else "#"
    return result


def new_idea():
    machines = get_machines()
    total_presses = 0
    
    for machine in machines:
        lights, buttons, _ = machine
        wanted_lights = lights
        lights_possible = ["".join(["." for x in range(len(lights))])]
        buttons_pressed = 0
        while wanted_lights not in lights_possible:
            buttons_pressed += 1
            new_lights_possible = []
            for lights in lights_possible:
                for button in buttons:
                    new_lights_possible.append(apply_button(lights, button))
            lights_possible = new_lights_possible
        total_presses += buttons_pressed
        

    print(f"Part 1 result: {total_presses}")



def main():
    new_idea()

if __name__ == "__main__":
    main()