import csv

with open("../data.csv", "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')

    positions = []
    for row in reader:
        positions.append((row[0], int(row[1])))

def problem1():
    horizontal, depth = 0, 0

    for move, distance in positions:
        if move == "forward":
            horizontal += distance
        if move == "down":
            depth += distance
        if move == "up":
            depth -= distance

    print(f"Result {horizontal * depth}")

def problem2():
    aim = 0 
    horizontal = 0
    depth = 0 

    for move, distance in positions:
        if move == "down":
            aim += distance
        if move == "up":
            aim -= distance
        if move == "forward":
            horizontal += distance
            depth += aim * distance

    print(f"Result 2 {horizontal * depth}")

if __name__ == '__main__':
    problem1()
    problem2()