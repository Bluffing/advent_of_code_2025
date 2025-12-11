def main():
    with open('day2_input.txt') as file:
        for line in file:
            split = line.split(',')
    
    counter = 0
    for s in split:
        bloo = s.split('-')
        for i in range(int(bloo[0]), int(bloo[1])+1):
            num_string = str(i)
            if len(num_string)%2 != 0:
                continue

            mid = int(len(num_string)/2)
            uno = num_string[:mid]
            dos = num_string[mid:]

            if uno == dos:
                counter+=i
    print('counter : ' + str(counter))

def main_2():
    with open('day2_input.txt') as file:
    # with open('day2_input_test.txt') as file:
        for line in file:
            split = line.split(',')
    
    counter = 0
    for s in split:
        bloo = s.split('-')
        print(bloo)
        max_string_length = len(bloo[1])
        for i in range(int(bloo[0]), int(bloo[1])+1):
            num_string = str(i)
            for num_split_amount in range(2,max_string_length):
                if len(num_string)%num_split_amount != 0:
                    continue

                correct = True
                numos = int(len(num_string)/num_split_amount)
                main = num_string[0:numos]

                for j in range(1,num_split_amount):
                    substring = num_string[j*numos:(j+1)*numos]
                    if main != substring:
                        correct = False
                        break

                if correct:
                    counter+=i
                    break

    print('counter : ' + str(counter))

main_2()