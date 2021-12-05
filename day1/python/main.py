with open("../data.txt", "r") as f:
    lines = f.readlines()


def problem1():
    larger_measurements = 0
    previous_measurement = 0

    for i, number in enumerate(lines):
        measurement = int(number)
        if i == 0:
            previous_measurement = measurement
            continue

        if measurement > previous_measurement:
            larger_measurements += 1
        
        previous_measurement = measurement

    print(larger_measurements)

def problem2():
    int_lines = list(map(int, lines))
    count = sum(a < b for a, b in zip(int_lines, int_lines[3:]))
    print(count)

if __name__ == '__main__':
    problem1()
    problem2()