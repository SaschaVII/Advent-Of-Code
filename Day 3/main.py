def get_lines() -> list[str]:
    content = []
    with open("Day 3/data.txt", "r") as file:
        content = file.read()
    return content.split("\n")

def highest_from_left(bank: str, start: int = 0, end: int = 0) -> tuple[int, int]:
    highest = int(bank[start])
    index = start

    for i in range(start, end if end != 0 else len(bank)):
        current = int(bank[i]) 
        if current > highest:
            highest = current   
            index = i

    return (highest, index)

def get_highest_joltage(bank: str) -> int:
    print("calculating max joltage for:", bank)

    last_index = -1
    result = ""
    for i in range(12):
        highest, index = highest_from_left(bank, start = last_index + 1, end = len(bank) - (11 - i))
        result += str(highest)
        last_index = index

    print("highest joltage for bank:", result)
    return int(result)

def main():
    banks = get_lines()
    max_joltage: int = 0

    for bank in banks:
        max_joltage += get_highest_joltage(bank)
        print()
    
    print("Result:", max_joltage)

if __name__ == "__main__":
    main()