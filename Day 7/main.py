import pathlib as pl
from functools import reduce

def get_lines() -> list[str]:
    content = []
    # path = str(pl.Path(__file__).parent.resolve()) + "/data_tests.txt"
    path = str(pl.Path(__file__).parent.resolve()) + "/data.txt"
    with open(path, "r") as file:
        print(f"reading file contents of \"{path}\"")
        content = file.read()
    return content.split("\n")


def day_1():
    layers = get_lines()
    split_count = 0
    beam_locations: set[int] = {layers[0].find("S")}
    for i in range(1, len(layers)):
        new_beam_locations = beam_locations.copy()
        for beam_location in beam_locations:
            if layers[i][beam_location] == "^":
                split_count += 1
                new_beam_locations.remove(beam_location)
                if beam_location < len(layers[i]) - 1 and beam_location+1 : new_beam_locations.add(beam_location+1)
                if beam_location > 0 and beam_location-1: new_beam_locations.add(beam_location-1)
        beam_locations = new_beam_locations
    print(f"Day 1 result: {split_count}")

def day_2():
    layers = get_lines()
    memo:dict[tuple[int, int], int] = {(0,0): 0}

    def calculate_options(beam_location: int, layer_index) -> int:
        if memo.get((beam_location, layer_index), None) is not None:
            return memo[(beam_location, layer_index)]
        if layer_index == len(layers): 
            memo[(beam_location, layer_index)] = 1
            return 1
        if layers[layer_index][beam_location] == ".":
            result = calculate_options(beam_location, layer_index+1)
            memo[(beam_location, layer_index)] = result
            return result
        if layers[layer_index][beam_location] == "^":
            result = calculate_options(beam_location+1, layer_index+1) + calculate_options(beam_location-1, layer_index+1)
            memo[(beam_location, layer_index)] = result
            return result
        print("Should nerver reach here!!")
        return 0
    
    option_count = calculate_options(layers[0].find("S"), 1)    
        
    print(f"Day 2 result: {option_count}")


def main():
    day_1()
    day_2()


if __name__ == "__main__":
    main()