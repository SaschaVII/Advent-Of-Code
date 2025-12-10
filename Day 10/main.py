import pathlib as pl

# returns a list of machines tuples
def get_machines() -> list[tuple[str, list[set[int]], list[int]]]:
    content = []
    result: list[tuple[str, list[set[int]], list[int]]] = []
    path = str(pl.Path(__file__).parent.resolve()) + "/data_tests.txt"
    # path = str(pl.Path(__file__).parent.resolve()) + "/data.txt"

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


def lights_after_button(lights: str, button: set[int]) -> str:
    result = ""
    for i in range(len(lights)):
        if i not in button: result+= lights[i]
        else: result += "." if lights[i] == "#" else "#"
    return result


def get_fewest_presses(lights_wanted: str, current_lights: str, buttons_remaining: list[set[int]]) -> int:
    level = 0
    if current_lights == lights_wanted:
        return level
    
    level += 1
    # first level
    for button in buttons_remaining:
        if lights_after_button(current_lights, button) == lights_wanted:
            return level

    level += 1        
    # second level
    for button in buttons_remaining:
        if lights_after_button(current_lights, button) == lights_wanted:
            return level


def lights_match(lights: str, buttons_pressed: list[set[int]]) -> bool:
    resulting_lights: str = ""
    for i in range(len(lights)):
        count = 0
        for button in buttons_pressed:
            count += 1 if i in button else 0
        resulting_lights += "." if count % 2 == 0 else "#"
    return lights == resulting_lights   


def part_1():
    machines = get_machines()
    
    for machine in machines:
        print(f"finding solution for {lights}")
        lights, buttons, joltages = machine
        current_lights = "".join(["." for x in range(len(lights))])
        fewest_presses = get_fewest_presses(lights, current_lights, buttons)
        for button in buttons:
            lights_match()
        print(f"number of button necessary: {fewest_presses}")
        print()
        



def main():
    part_1()

if __name__ == "__main__":
    main()