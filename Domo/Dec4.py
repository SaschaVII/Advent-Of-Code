def countAdjacentRolls(boolMap):
    count = 0
    for rows in boolMap:
        for columns in rows: 
            count += columns
    return count - 1  # Exclude the center position itself

def getNumberOfRolls(boolMap, total = 0):
    length_total = len(boolMap)
    another_run = False
    for row in range(length_total):
        length_line = len(boolMap[row])
        for column  in range(length_line):

            sliceRowLower = row -1 if (row -1) >= 0 else 0
            sliceRowUpper = row + 2 if (row +1) <= length_line else length_line
            sliceColumnLower = column -1 if (column -1) >= 0 else 0
            sliceColumnUpper = column + 2 if (column +1) <= length_total else length_total

            slice = [x[sliceColumnLower:sliceColumnUpper] for x in boolMap[sliceRowLower:sliceRowUpper]]
            if boolMap[row][column] == 1 and countAdjacentRolls(slice) < 4:
                
                total += 1
                another_run = True
                boolMap[row][column] = 0

    if not another_run:
        return total
    return getNumberOfRolls(boolMap, total)


if __name__ == '__main__':

    file_path = 'inputTest.txt'

    with open(file_path, 'r') as file:

        lines = file.readlines()

    boolMap = [[0 for x in range(len(lines))] for y in range(len(lines[0].strip()))] 

    for row in range(len(lines)):
        length_line = len(lines[row].strip())
        for column  in range(length_line):
            if lines[row][column] == "@":
                boolMap[row][column] = 1


    print(getNumberOfRolls(boolMap))