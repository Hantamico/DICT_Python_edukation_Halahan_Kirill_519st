import random
from random import choice


first = 0
second = 0
ar = 0
res = 0
mark = 0
count = 0
status = 1
level = 0


def start():
    global first, second, ar
    first = random.choice(range(2, 10))
    second = random.choice(range(2, 10))
    ar = choice(["+", "-", "*"])


def start_res():
    global first, second, ar, res
    start()
    if ar == '+':
        print(str(first) + ' + ' + str(second))
        res = first + second
    elif ar == '-':
        print(str(first) + ' - ' + str(second))
        res = first - second
    elif ar == '*':
        print(str(first) + ' * ' + str(second))
        res = first * second


def lvl_2():
    global second, res
    second = choice(range(11, 30))
    res = second ** 2
    print(second)
    level = 2


def result():
    global mark, count, status
    if res == answer:
        print('Right!')
        mark += 1
        count += 1
        status = 1
    else:
        print('Wrong!')
        count += 1
        status = 1


def main():
    global answer, status, level
    choose_level = input("choose level 1 or 2")
    while count != 5:
        if choose_level == "1":
            level = 1
            try:
                start_res()
                answer = int(input(">"))
                result()
            except ValueError:
                print("Incorrect format")
                status = 0
        elif choose_level == "2":
            lvl_2()
    print('Your mark is ' + str(mark) + '/5')
    print("Would you like to save the result? Enter yes or no.")
    answer_file = input()
    if answer_file == 'YES' or 'Yes' or 'y' or 'yes':
        name = input('What is your name? \n')
        file = open('results.txt', 'w')
        file.write(name + ':' + str(mark) + '/5 ' + 'in level ' + str(level) + '\n')
        file.close()
        print('The results are saved in "results.txt".')


if __name__ == '__main__':
    main()
