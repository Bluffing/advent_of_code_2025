def main():
    counter = 0
    with open('day3_input.txt') as file:
        for line in file:
            line = line.strip()
            max = 0
            for i in range(0, len(line)-1):
                for j in range(i+1, len(line)):
                    num = int(line[i] + line[j])
                    if num > max:
                        max = num
            # print(line + ' : ' + str(max))
            counter += max
    print('counter : ' + str(counter))

def main_2():
    counter = 0
    with open('day3_input.txt') as file:
    # with open('day3_input_test.txt') as file:
        for line in file:
            line = [int(c) for c in line.strip()]
            max = ''
            last_char_idx = -1

            for i in range(0, 12):
                max_num = 0
                for j in range(last_char_idx+1, len(line)-(11 - i)):
                    if line[j] > max_num:
                        max_num = line[j]
                        last_char_idx = j
                max += str(max_num)

            # print(''.join([str(c) for c in line]) + ' : ' + max)
            counter += int(max)
    print('counter : ' + str(counter))

main_2()