import math


def main():
    counter = 0
    lines = []
    nums = []
    signs = []
    # with open('day6_input_test.txt') as file:
    with open("day6_input.txt") as file:
        for line in file:
            lines.append(line.strip().split())

    first = True
    for l in lines[0:-1]:
        for i, n in enumerate(l):
            if first:
                nums.append([])
            nums[i].append(int(n))
        first = False
    signs = lines[-1]

    for i, s in enumerate(signs):
        total = nums[i][0]
        for n in nums[i][1:]:
            if s == "*":
                total *= n
            else:
                total += n
        counter += total

    print(counter)


def main_2():
    nums = []
    signs = []
    # with open('day6_input_test.txt') as file:
    with open("day6_input.txt") as file:
        for line in file:
            if line[0] == "*" or line[1] == "+":
                signs = line.split()
                continue

            line = list(line)
            if line[-1] == "\n":
                line = line[:-1]
            nums.append(line)
    # print(f'nums : {str(nums)}')
    # print(f'signs : {str(signs)}')

    counter = 0
    total = 1 if signs[0] == "*" else 0
    idx = 0
    for col in range(len(nums[0])):
        n = "".join([l[col] for l in nums])
        if n.strip() == "":
            counter += total
            idx += 1
            total = 1 if signs[idx] == "*" else 0
            continue
        if signs[idx] == "*":
            total *= int(n)
        else:
            total += int(n)

    counter += total
    print(counter)


def main_3():
    # with open('day6_input_test.txt') as file:
    with open("day6_input.txt") as file:
        nums = [[c] if c != " " else [] for c in file.readline() if c != "\n"]

        for line in file:
            if line[0] == "*" or line[1] == "+":
                signs = line.split()
                continue

            # if line[-1] == '\n':
            # line = line[:-1]

            for i, c in enumerate(line[:-1]):
                if c != " ":
                    nums[i].append(c)

    # print(f'nums : {str(nums)}')
    # print(f'signs : {str(signs)}')

    counter = 0

    mult = True if signs[0] == "*" else False
    total = 1 if mult else 0

    idx = 0
    for n in nums:
        if len(n) == 0:
            counter += total
            idx += 1
            mult = True if signs[idx] == "*" else False
            total = 1 if mult else 0
            continue

        n = int("".join(n))
        if mult:
            total *= n
        else:
            total += n

    counter += total
    print(counter)


def main_4():
    nums = []
    line_size = 0
    num_lines = 0
    # with open("day6_input_test.txt") as file:
    with open("day6_input.txt") as file:
        for line in file:
            if line[0] == "*" or line[1] == "+":
                signs = line.split()
                continue

            nums += list(line[:-1])
            line_size = len(line) - 1
            num_lines += 1

    # print(f"nums : {str(nums)}")
    # print(f'signs : {str(signs)}')

    counter = 0
    idx = 0

    mult = True if signs[0] == "*" else False
    total = 1 if mult else 0

    temp_arr = [""] * num_lines

    for col in range(line_size):
        smt = False
        for row in range(num_lines):
            a = nums[col + line_size * row]
            if a != " ":
                temp_arr[row] = a
                smt = True
            else:
                temp_arr[row] = ""

        if not smt:
            counter += total
            idx += 1
            mult = True if signs[idx] == "*" else False
            total = 1 if mult else 0
            continue

        n = int("".join(temp_arr))
        total = total * n if mult else total + n

    counter += total
    print(counter)


from datetime import datetime

# startTime = datetime.now()
# print()
# main_2()
# print(f"2 : {(datetime.now() - startTime).microseconds / 1000} ms")
# print()
#
# startTime = datetime.now()
# main_3()
# print(f"3 : {(datetime.now() - startTime).microseconds / 1000} ms")
# print()

startTime = datetime.now()
main_4()
print(f"4 : {(datetime.now() - startTime).microseconds / 1000} ms")
print()
