def main():
    current = 50
    counter = 0

    with open('day1_input.txt') as file:
        for line in file:
            num = int(line[1:])
            temp = current

            if line.startswith('L'):
                if current == 0:
                    counter -= 1

                current -= num
                while current < 0:
                    current += 100
                    counter += 1

                if current == 0:
                    counter += 1
            else:
                current += num
                while current > 99:
                    current -= 100
                    counter += 1

            print(f"{line.removesuffix('\n')}\t: {str(temp)} -> {str(current)}\t: {str(counter)}")

    print('res : ' + str(counter) + ' : ' + str(current))

main()