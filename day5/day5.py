def main():
    counter = 0
    checker = []
    checkee = []
    # with open('day5_input_test.txt') as file:
    with open('day5_input.txt') as file:
        first_step = True
        for line in file:
            line = line.strip()
            if line == '':
                first_step = False
                continue

            if first_step:
                checker.append([int(n) for n in line.split('-')])
            else:
                checkee.append(int(line))
    # print(checker)
    # print(checkee)
    for e in checkee:
        for r in checker:
            if e >= r[0] and e <= r[1]:
                counter += 1
                break
    print(counter)

def main_2():
    counter = 0
    checker = []
    # with open('day5_input_test.txt') as file:
    with open('day5_input.txt') as file:
        for line in file:
            line = line.strip()
            if line == '':
                break
            checker.append([int(n) for n in line.split('-')])

    checker.sort(key=lambda c: c[0])

    for i, c in enumerate(checker):
        bounds = [[c[0], c[1]]]
        for j in range(i):
            c_lower = checker[j][0]
            c_upper = checker[j][1]

            added_bounds = []
            for b in reversed(bounds):
                lower_bound = b[0]
                upper_bound = b[1]

                # lb -- cl -- cu -- ub
                if lower_bound < c_lower and upper_bound > c_upper:
                    bounds.remove(b)
                    added_bounds.append([lower_bound, c_lower-1])
                    added_bounds.append([c_upper+1, upper_bound])
                    break

                changed = False
                # cl -- lb -- cu
                if lower_bound >= c_lower and lower_bound <= c_upper: 
                    lower_bound = c_upper + 1
                    changed = True
                    # print(f'new lower : {lower_bound}')

                # cl -- ub -- cu
                if upper_bound >= c_lower and upper_bound <= c_upper: 
                    upper_bound = c_lower - 1
                    changed = True
                    # print(f'new upper : {upper_bound}')

                if changed:
                    bounds.remove(b)
                    if lower_bound <= upper_bound:
                        added_bounds.append([lower_bound, upper_bound])
                    break


            for ab in added_bounds:
                bounds.append(ab)
        # print(bounds)
        for b in bounds:
            counter += b[1]-b[0]+1
    print(counter)
            
from datetime import datetime
startTime = datetime.now()

main_2()

print(f"{(datetime.now() - startTime).microseconds / 1000} ms")