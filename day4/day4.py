def main():
    counter = 0
    map = []
    # with open('day4_input_test.txt') as file:
    with open('day4_input.txt') as file:
        for line in file:
            map.append(list(line.strip()))

    height = len(map)
    width = len(map[0])

    for y in range(height):
        for x in range(width):
            if map[y][x] != '@':
                continue

            num_adj_rolls = 0

            if y > 0:
                if x > 0 and map[y-1][x-1] == '@':
                    num_adj_rolls += 1
                if map[y-1][x] == '@':
                    num_adj_rolls += 1
                if x < width-1 and map[y-1][x+1] == '@':
                    num_adj_rolls += 1

            if x > 0 and map[y][x-1] == '@':
                num_adj_rolls += 1
            if x < width-1 and map[y][x+1] == '@':
                num_adj_rolls += 1

            if y < height-1:
                if x > 0 and map[y+1][x-1] == '@':
                    num_adj_rolls += 1
                if map[y+1][x] == '@':
                    num_adj_rolls += 1
                if x < width-1 and map[y+1][x+1] == '@':
                    num_adj_rolls += 1
        
            if num_adj_rolls < 4:
                counter += 1
    print('counter : ' + str(counter))

def main_2():
    counter = 0
    map = []
    # with open('day4_input_test.txt') as file:
    with open('day4_input.txt') as file:
        for line in file:
            map.append(list(line.strip()))

    height = len(map)
    width = len(map[0])

    found = True
    while found:
        found = False
        for y in range(height):
            for x in range(width):
                if map[y][x] != '@':
                    continue

                num_adj_rolls = 0

                if y > 0:
                    if x > 0 and map[y-1][x-1] == '@':
                        num_adj_rolls += 1
                    if map[y-1][x] == '@':
                        num_adj_rolls += 1
                    if x < width-1 and map[y-1][x+1] == '@':
                        num_adj_rolls += 1

                if x > 0 and map[y][x-1] == '@':
                    num_adj_rolls += 1
                if x < width-1 and map[y][x+1] == '@':
                    num_adj_rolls += 1

                if y < height-1:
                    if x > 0 and map[y+1][x-1] == '@':
                        num_adj_rolls += 1
                    if map[y+1][x] == '@':
                        num_adj_rolls += 1
                    if x < width-1 and map[y+1][x+1] == '@':
                        num_adj_rolls += 1
            
                if num_adj_rolls < 4:
                    counter += 1
                    map[y][x] = 'x'
                    found = True
    print('counter : ' + str(counter))

from datetime import datetime
startTime = datetime.now()

main_2()


# timer = (datetime.now() - startTime).microseconds / 1000
print(f"{(datetime.now() - startTime).microseconds / 1000} ms")