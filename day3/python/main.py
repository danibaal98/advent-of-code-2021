from typing import List


with open("../data.txt", "r") as f:
    input_data = [x.strip() for x in f.readlines()]

def invert_binary(number):
    temp = int(number, 2)
    inverse = temp ^ (2 ** (len(number) + 1) - 1)

    return str(bin(inverse)[3:])

def rating(data: List, position: int, is_most_common: bool) -> int:
    if len(data) == 1:
        return int(data[0], 2)
    
    one_occurrences = sum([int(binary_number[position]) for binary_number in data if binary_number[position] == "1"])
    same_occurrences = one_occurrences == len(data) / 2
    more_ones = one_occurrences > len(data) / 2

    new_data = []

    if is_most_common:
        if more_ones or same_occurrences:
            new_data = [binary_number for binary_number in data if binary_number[position] == "1"]
        else:
            new_data = [binary_number for binary_number in data if binary_number[position] == "0"]
    else:
        if more_ones or same_occurrences:
            new_data = [binary_number for binary_number in data if binary_number[position] == "0"]
        else:
            new_data = [binary_number for binary_number in data if binary_number[position] == "1"]

    return rating(new_data, position + 1, is_most_common)


def problem1():
    one_occurrences = [0] * len(input_data[0])

    for binary_number in input_data:
        for i, bit in enumerate(binary_number):
            if bit == "1":
                one_occurrences[i] += 1

    gamma = ""
    for occurrence in one_occurrences:
        if occurrence > len(input_data) / 2:
            gamma += "1"
            continue
        gamma += "0"

    epsilon = invert_binary(gamma)

    print(gamma, epsilon)

    n_gamma = int(gamma, 2)
    n_epsilon = int(epsilon, 2)

    print(f"Result {n_gamma * n_epsilon}")


def problem2():
    oxygen = rating(input_data, 0, True)
    co2 = rating(input_data, 0, False)
    print(oxygen * co2)

if __name__ == '__main__':
    problem1()
    problem2()