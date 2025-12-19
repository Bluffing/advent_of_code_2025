def main():
    counter = 0
    # with open('dayxz_input_test.txt') as file:
    with open("dayxz_input.txt") as file:
        for line in file:
            line = line.strip()
            print(line)
    return counter


def main_2():
    counter = 0
    # with open('dayxz_input_test.txt') as file:
    with open("dayxz_input.txt") as file:
        for line in file:
            line = line.strip()
            print(line)
    return counter


import timeit

print(f"1 : {timeit.timeit(main, number=1000)} ms")
print(main())

print(f"2 : {timeit.timeit(main_2, number=1000)} ms")
print(main_2())
