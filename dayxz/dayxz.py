def main():
    counter = 0
    # with open('dayxz_input_test.txt') as file:
    with open('dayxz_input.txt') as file:
        for line in file:
            line = line.strip()
            print(line)
    print(counter)

def main_2():
    counter = 0
    # with open('dayxz_input_test.txt') as file:
    with open('dayxz_input.txt') as file:
        for line in file:
            line = line.strip()
            print(line)
    print(counter)
            
from datetime import datetime
startTime = datetime.now()

main()
# main_2()

print(f"{(datetime.now() - startTime).microseconds / 1000} ms")