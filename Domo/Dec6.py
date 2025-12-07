import numpy as np

def getMult(list_of_numbers):
    total = 1
    for number in list_of_numbers:
        total *= number
    return total

def getPlus(list_of_numbers):
    total = 0
    for number in list_of_numbers:
        total += number
    return total

def getLineTotal(list_of_numbers, operator):
    if operator == "+":
        return getPlus(list_of_numbers)
    return getMult(list_of_numbers)


if __name__ == '__main__':

    file_path = 'inputTest.txt'

    with open(file_path, 'r') as file:

        lines = file.readlines()

    list_of_columns = []
    total = 0
    transposed_columns = []
    operator_line = []
#Part 1:
    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        
        
        # Split by minus to get individual pairs
        parts = line.split()
        current_line = []
        for part in parts:

            if "*" in part or "+" in part:
                operator_line.append(part)
            else:
                current_line.append(int(part))
        if current_line:
            list_of_columns.append(current_line)

    print("lines:  ",len(lines))
    print("columns:  ",len(lines[0]))

    numbers_tuple = []

    all_tuples = []

    for col in range(len(lines[0])-1):
        number_str = []
        for row in range(len(lines)-1):
            number_str.append(lines[row][col])
        
        whitespaces_amount = number_str.count(" ")
        if (whitespaces_amount < 4):
            numbers_tuple.append(int(''.join(number_str)))
        else:
            all_tuples.append(numbers_tuple)
            numbers_tuple = []
    all_tuples.append(numbers_tuple)
        
    transposed_columns = np.transpose(list_of_columns)
    i = 0
    for operator in operator_line:
        total += getLineTotal(all_tuples[i],operator)
        i+=1

    # print(transposed_columns)
    # print(operator_line)
    print(total)