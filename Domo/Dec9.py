import numpy as np

NO_TILE = 0
RED_TILE = 1
GREEN_TILE = 2

def checkIfRectangleGreen(tiles_map, corner1, corner2):
    row1 = corner1[1]
    row2 = corner2[1]
    col1 = corner1[0]
    col2 = corner2[0]

    row_increment = 1 if row2 > row1 else -1
    col_increment = 1 if col2 > col1 else -1


    #left and right col
    for r in range(row1+row_increment, row2, row_increment):
        if tiles_map[r][col1+col_increment] == GREEN_TILE or tiles_map[r][col1+col_increment] == RED_TILE:
            return True
        if tiles_map[r][col2-col_increment] == GREEN_TILE or tiles_map[r][col2-col_increment] == RED_TILE:
            return True
        
    #top and bottom row
    for c in range(col1+col_increment, col2, col_increment):
        if tiles_map[row1+row_increment][c] == GREEN_TILE or tiles_map[row1+row_increment][c] == RED_TILE:
            return True
        if tiles_map[row2-row_increment][c] == GREEN_TILE or tiles_map[row2-row_increment][c] == RED_TILE:
            return True

    return False

def getRectangleSize(corner1, corner2):
    return (abs(corner1[0]-corner2[0])+1)*(abs(corner1[1]-corner2[1])+1)

def colorEdgesGreen(tiles_map, red_tiles):
    for i in range(len(red_tiles)):
        x = red_tiles[i][0]
        y = red_tiles[i][1]
        prev_x = red_tiles[i-1][0]
        prev_y = red_tiles[i-1][1]

        if prev_x == x:
            increment = 1 if prev_y > y else -1
            for j in range (y+ increment, prev_y,increment):
                tiles_map[j][x] = GREEN_TILE

        elif prev_y == y:
            increment = 1 if prev_x > x else -1
            for j in range (x+increment, prev_x, increment):
                tiles_map[y][j] = GREEN_TILE


if __name__ == '__main__':

    file_path = 'inputTest.txt'

    red_tiles = []
    map_size = 100000
    tiles_map = np.zeros((map_size,map_size))

    with open(file_path, 'r') as file:

        lines = file.readlines()
        for line in lines:
            single_coordinate = []
            for number in line.split(','):
                single_coordinate.append(int(number))
                
            red_tiles.append(single_coordinate)

            print(single_coordinate)
            tiles_map[single_coordinate[1]][single_coordinate[0]] = RED_TILE

    #part 1
    largest_area = 0
    for i in range(len(red_tiles)):
        for j in range(len(red_tiles)):
            if i>= j:
                continue
            area = getRectangleSize(red_tiles[i], red_tiles[j])
            if area > largest_area:
                largest_area = area
    print("largest: ", largest_area)

    #part 2
    largest_only_green = 0
    colorEdgesGreen(tiles_map, red_tiles)
 
    for i in range(len(red_tiles)):
        for j in range(len(red_tiles)):
            if i>= j:
                continue
            
            area = getRectangleSize(red_tiles[i], red_tiles[j])
            if area > largest_only_green and not checkIfRectangleGreen(tiles_map,red_tiles[i], red_tiles[j]):               
                largest_only_green = area
    
    print("part 2: ", largest_only_green)