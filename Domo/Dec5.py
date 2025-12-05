if __name__ == '__main__':

    file_path = 'inputTest.txt'

    with open(file_path, 'r') as file:

        lines = file.readlines()

    list_of_ranges = []
    total = 0

    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        if "-" in line:
            # Split by minus to get individual pairs
            parts = line.split('-')
            list_of_ranges.append([int(parts[0]),int(parts[1])])
        else:
            break

    sorted_ranges = sorted(list_of_ranges, key = lambda number: number)

    for i in range(len(sorted_ranges)-1):
        if sorted_ranges[i][1] >= sorted_ranges[i+1][0]:
            if (sorted_ranges[i][1] > sorted_ranges[i+1][1]):
                sorted_ranges[i+1][1] = sorted_ranges[i][1]
            sorted_ranges[i][1] = sorted_ranges[i+1][0] -1
        total += sorted_ranges[i][1] - sorted_ranges[i][0] + 1
    total += sorted_ranges[len(sorted_ranges)-1][1] - sorted_ranges[len(sorted_ranges)-1][0] + 1
    print(total)