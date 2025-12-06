import pathlib as pl
from functools import reduce

def get_lines() -> list[str]:
    content = []
    # path = str(pl.Path(__file__).parent.resolve()) + "/data_tests.txt"
    path = str(pl.Path(__file__).parent.resolve()) + "/data.txt"
    with open(path, "r") as file:
        print(f"reading file contents of \"{path}\"")
        content = file.read()
    return content.split("\n")


def split_data(data: list[str]) -> tuple[list[str], list[str]]:
    return (data[:-1], str.split(data[-1])) 


def pivot_problems(problems) -> list[list[int]]:
    problems_pivoted: list[list[int]] = []

    for i in range(len(str.split(problems[0]))):
        problems_pivoted.append([])

    for line in problems:
        numbers = str.split(line)
        for j in range(len(numbers)):
            problems_pivoted[j].append(int(numbers[j]))

    return problems_pivoted


def day_1():
    problems_in_lines, operations = split_data(get_lines())
    problems = pivot_problems(problems_in_lines)
    problem_results = []
    result = 0

    for i in range(len(operations)):
        problem_result = 0
        if operations[i] == "+":
            for number in problems[i]:
                problem_result += number
        if operations[i] == "*":
            problem_result = 1
            for number in problems[i]:
                problem_result *= number
        problem_results.append(problem_result)

    for problem_result in problem_results:
        result += problem_result
    
    print("Day 1 Result:", result)


def day_2():
    problems_in_lines, operations = split_data(get_lines())
    row_length = len(problems_in_lines[0])
    result = 0

    problem = []
    current_operation = len(str.split(problems_in_lines[0])) - 1
    for x in range(row_length-1, -1, -1):
        num = ""
        for y in range(len(problems_in_lines)):
            char = problems_in_lines[y][x]
            if char != " ":
                num += char
        if len(num) > 0:
            problem.append(int(num))
        if len(num) == 0 or (x == 0 and y == len(problems_in_lines)-1):
            if operations[current_operation] == "+":
                result += reduce(lambda x,y : x+y, problem)
            if operations[current_operation] == "*":
                result += reduce(lambda x,y : x*y, problem)
            problem.clear()
            current_operation -= 1
    
    print("Day 2 Result:", result)


def main():
    day_1()
    day_2()


if __name__ == "__main__":
    main()