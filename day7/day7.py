def main():
    counter = 0
    # with open("day7_input_test.txt") as file:
    with open("day7_input.txt") as file:
        prev_line = list(file.readline().strip())
        width = len(prev_line)

        for line in file:
            line = list(line.strip())

            for i, c in enumerate(line):
                if prev_line[i] == "|" or prev_line[i] == "S":
                    if c == "^":
                        if i > 0:
                            line[i - 1] = "|"
                        if i < width - 1:
                            line[i + 1] = "|"
                        counter += 1
                    else:
                        line[i] = "|"
            prev_line = line
    return counter


def main_2():
    with open("day7_input.txt") as file:
        # with open("day7_input_test.txt") as file:
        lines = [list(l.strip()) for l in file.readlines()]

    possibilities = [0] * len(lines[0])
    possibilities[len(lines[0]) // 2] = 1

    for row in range(len(lines) - 1):
        current = lines[row]
        next = lines[row + 1]

        # print(f"current : {current}")
        # print(f"next    : {next}")

        for i, n in enumerate(next):
            if current[i] == "|" or current[i] == "S":
                if n == "^":
                    next[i - 1] = "|"
                    possibilities[i - 1] += possibilities[i]

                    next[i + 1] = "|"
                    possibilities[i + 1] += possibilities[i]

                    possibilities[i] = 0
                else:
                    next[i] = "|"
    return sum(possibilities)


def main_3():
    with open("day7_input.txt") as file:
        # with open("day7_input_test.txt") as file:

        current = list(file.readline()[:-1])
        possibilities = [0] * len(current)
        possibilities[len(current) // 2] = 1

        for l in file:
            if l[-1] != "\n":
                return sum(possibilities)

            next = list(l[:-1])

            # print(f"current : {current}")
            # print(f"next    : {next}")

            for i, n in enumerate(next):
                if current[i] == "|" or current[i] == "S":
                    if n == "^":
                        next[i - 1] = "|"
                        possibilities[i - 1] += possibilities[i]

                        next[i + 1] = "|"
                        possibilities[i + 1] += possibilities[i]

                        possibilities[i] = 0
                    else:
                        next[i] = "|"
            current = next


import timeit

print(f"1 : {timeit.timeit(main_2, number=1000)} ms")
print(main())

print(f"2 : {timeit.timeit(main_2, number=1000)} ms")
print(main_2())

print(f"3 : {timeit.timeit(main_3, number=1000)} ms")
print(main_3())
