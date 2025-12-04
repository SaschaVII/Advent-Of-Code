def getHighestNumber(digits):
    highest = -1
    index = 0
    returnedIndex = 0
    for d in digits:
        
        if int(d) > highest:
            highest = int(d)
            returnedIndex = index
        index += 1
    return (highest, returnedIndex)


if __name__ == '__main__':

    file_path = 'inputTest.txt'

    with open(file_path, 'r') as file:

        lines = file.readlines()
    
    total = 0
    digits = [0]*12
    for line in lines:
        line = line.strip()
        if not line:
            continue
        j = 0
        for i in range(12):

            print(line[i+j:len(line)-11+i])
            highest_tuple = getHighestNumber(line[i+j:len(line)-11+i])
            digits[i] = highest_tuple[0]
            j += highest_tuple[1]
            print("index :  ", j)

        print(digits)

        total += int(''.join(map(str, digits)))



    print(total)

   

