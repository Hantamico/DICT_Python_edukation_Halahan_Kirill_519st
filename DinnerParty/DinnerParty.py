print('Enter the number of friends joining (including you):')
number_of_friends = int(input())
members = {}
if number_of_friends >= 0:
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(number_of_friends):
        name = input(">")
        members[name] = 0
else:
    print('No one is joining for the party')
print('Enter the total amount:')
all_amount = int(input())
amount = round(all_amount / number_of_friends, 2)
for name in members:
    members[name] = amount
print(members)
