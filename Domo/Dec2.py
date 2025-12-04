def checkNumberforRepition(number, repition ):
    if len(str(number))%repition != 0:
        return False
    firstPart = str(number)[:len(str(number))//repition]
    for i in range(1, repition):
        if firstPart != str(number)[i*len(firstPart):(i+1)*len(firstPart)]:
            return False
    return True
def checkNumberforInvalidId(number):
    length  = len(str(number))
    for i in range (2, length +1):
        if checkNumberforRepition(number, i):
            return number

    return 0

if __name__ == '__main__':
    file_path = 'inputDay2'

    with open(file_path, 'r') as file:

        lines = file.readlines()
    
    total = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Split by comma to get individual pairs
        for pair_str in line.split(','):
            pair_str = pair_str.strip()
            if '-' in pair_str:
                # Split by hyphen to get the two numbers
                parts = pair_str.split('-')
                for num in range(int(parts[0]), int(parts[1]) + 1):
                    total += checkNumberforInvalidId(num)

                    if checkNumberforInvalidId(num):
                        print(f"Found invalid ID number: {num}")


    print(total)

   

