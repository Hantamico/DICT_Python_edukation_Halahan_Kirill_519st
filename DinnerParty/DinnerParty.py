from random import choice


number_of_friends = int(input('Enter the number of friends joining (including you):'))
members = {}
members_list = []
if number_of_friends >= 0:
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(number_of_friends):
        name = input(">")
        members[name] = 0
        members_list.append(name)
else:
    print('No one is joining for the party')
print('Enter the total amount:')
all_amount = int(input())
for name in members:
    members[name] = round(all_amount / number_of_friends, 2)
r_name = choice(members_list)
answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
if answer == 'Yes':
    print(r_name + ' is the lucky one!')
else:
    print('No one is going to be lucky')
