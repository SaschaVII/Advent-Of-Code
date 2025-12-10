import numpy as np
import itertools
import time
import math

def getBoolLights(led_lights):
    bool_lights = []
    for led_group in led_lights:
        bool_group = []
        for led in led_group:
            if led == ".":
                bool_group.append(0)
            elif led == "#":
                bool_group.append(1)
        bool_lights.append(bool_group)
    return bool_lights

def getIntButtons(button_list):
    int_buttons = []
    for button_line in button_list:
        int_line = []
        for button_group in button_line:

            int_group = []
            for button in button_group[1:-1].split(','):
                int_group.append(int(button))
        
            int_line.append(int_group)
        int_buttons.append(int_line)
    return int_buttons

def toggle(single_var):
    if single_var == 1:
        return 0
    return 1

def checkIfSolution(bool_group, button_subgroup):
    clone = bool_group.copy()
    for button in range(len(button_subgroup)):
        clone[button_subgroup[button]] = toggle(clone[button_subgroup[button]])
    if all(val == 0 for val in clone):
        return True
        #found solution
    return False


def getShortestPath(bool_group, button_line):
   
    for i in range(1,len(button_line)): # take more and more buttons from permutation
        combinations = itertools.combinations(button_line,i)
        for combination in combinations:
            flat_array = list(itertools.chain.from_iterable(combination))
            if checkIfSolution(bool_group, flat_array):

                print(combination)
                return i
            
    
    print("nerver should have gotten here")
    return 0


if __name__ == '__main__':

    file_path = 'inputTest.txt'
    led_lights =[]
    bool_lights = []
    button_list = []
    int_button_list = []
    joltages = []
    st = time.time()

    with open(file_path, 'r') as file:

        lines = file.readlines()
        for line in lines:
            i = 0
            button_line = []
            for element in line.split(' '):
                if i == 0:
                    led_lights.append(element)
                    
                elif i == len(line.split(' '))-1:
                    joltages.append(element)
                else:
                    button_line.append(element)
                i+=1
            button_list.append(button_line)

    bool_lights = getBoolLights(led_lights)
    int_button_list = getIntButtons(button_list)
    
    total = 0
    for i in range(len(bool_lights)):
        print("led: " , bool_lights[i], "   buttons: ", int_button_list[i])
        total += getShortestPath(bool_lights[i], int_button_list[i])
        #print("shortest path: " , getShortestPath(bool_lights[i], int_button_list[i]))
    print(total)
    et = time.time()
    print("execution time:  ", et -st)
