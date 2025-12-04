def goRight(baseValue, addedValue):
    # Always return only the last two digits as an integer.
    # Right movement: count how many times we wrap through 0.
    total = baseValue + addedValue
    crossings = total // 100  # Each complete 100 is one wrap/pass through 0
    return (total % 100, crossings)
        
def goLeft(baseValue, addedValue):
    # Always return only the last two digits as an integer using modulo 100.
    # Left movement: count how many times we wrap through 0 (going negative).
    total = baseValue - addedValue

    if total <= 0:
        # We went negative. Count wraps: how many times 100 do we need to add to get back to [0,99]?
        crossings = (abs(total) + 100) // 100  # Round up
    else:
        crossings = 0
    if baseValue == 0:
        crossings -=1
    return (total % 100, crossings)

if __name__ == '__main__':
    file_path = 'input.txt'

    with open(file_path, 'r') as file:

        lines = file.readlines()
    
    currentValue = 50
    numberOfZeros = 0

    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        
        direction = line[0].upper()
        if direction in ('L', 'R'):
            try:
                addedValue = int(line[1:].strip())
            except ValueError:
                print(f"Skipping invalid line: {raw!r}")
                continue
            if direction == 'L':
                currentValueAndZeros = goLeft(currentValue, addedValue)
                currentValue = currentValueAndZeros[0]
                numberOfZeros += int(currentValueAndZeros[1])
            else:
                currentValueAndZeros = goRight(currentValue, addedValue)
                currentValue = currentValueAndZeros[0]
                numberOfZeros += int(currentValueAndZeros[1])
        else:
            print("Error in input")
        print(line)
        print(f"Current Value: {currentValue}, Zeros Count Change: {currentValueAndZeros[1]}, Total Zeros: {numberOfZeros}")
    print(f"Final Value: {numberOfZeros}")

