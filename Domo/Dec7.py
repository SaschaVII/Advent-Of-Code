import numpy as np


EMPTY_SPACE = 0
SPLITTER = 1
BEAM = 2
STARTING_POINT = 3


if __name__ == '__main__':

    file_path = 'inputTest.txt'

    integer_map = []


    with open(file_path, 'r') as file:

        lines = file.readlines()
        for line in lines:
            integer_line = []
            for char in line:
                match char:
                    case ".":
                        integer_line.append(EMPTY_SPACE)

                    case "^":
                        integer_line.append(SPLITTER)

                    case "S":
                        integer_line.append(STARTING_POINT)
            integer_map.append(integer_line)
        print (integer_map)

    beam_strength_map = np.zeros((len(integer_map),len(integer_map[0])))

  
#Part 1:
    splits_total = 0
    for row in range(1,len(integer_map)):
        for col in range (len(integer_map[0])-1):
            char_on_top = integer_map[row-1][col]
            char_left = integer_map[row][col-1]
            char_right = integer_map[row][col+1]
            char_current = integer_map[row][col]

            beam_strength_top = beam_strength_map[row-1][col]

            if char_on_top != BEAM and char_on_top != STARTING_POINT:
                continue
            if char_current != SPLITTER:
                integer_map[row][col] = BEAM

                if char_on_top == STARTING_POINT:
                    beam_strength_map[row][col] = 1
                else:    
                    beam_strength_map[row][col] += beam_strength_top
                
                continue
            if char_current == SPLITTER:
                if col > 0:
                    integer_map[row][col-1] = BEAM
                    beam_strength_map[row][col-1] += beam_strength_top
                if col < len(integer_map[0]):
                    integer_map[row][col+1] = BEAM
                    beam_strength_map[row][col+1] += beam_strength_top
                splits_total +=1
    
    print (integer_map)
    print("splits total ", splits_total)
    print (beam_strength_map[:-1])
    print("total Beams:",sum(beam_strength_map[len(integer_map)-2]))