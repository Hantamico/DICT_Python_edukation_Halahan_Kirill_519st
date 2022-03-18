from random import choice

members = {}
members_list = []
name = 0
all_amount = 0
answer = 0
r_name = 0
number_of_friends = 0


def start():
    global name, all_amount, r_name, count
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(number_of_friends):
        name = input(">")
        members[name] = 0
        members_list.append(name)
    r_name = choice(members_list)
    print('Enter the total amount:')
    all_amount = int(input())
    for name in members:
        members[name] = round(all_amount / count, 2)


def choise_lucky():
    global name, r_name
    for name in members:
        if name != r_name:
            members[name] = round(all_amount / (count - 1), 2)
        else:
            members[name] = 0
    print(members)


try:
    count = int(input('Enter the number of friends joining (including you):\n'))
    if count <= 0:
        print('No one is joining for the party')
    else:
        start()
        answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
        if answer == 'Yes':
            print(str(r_name) + ' is the lucky one!\n')
            choise_lucky()
        else:
            print('No one is going to be lucky\n')
            print(members)
except ValueError:
    print('No one is joining for the party')
