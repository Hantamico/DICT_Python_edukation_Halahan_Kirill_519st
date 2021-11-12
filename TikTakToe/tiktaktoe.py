# print("X", "X", "O")
# print("0", "0", "X")
# print("X", "0", "X")


mat = input("Enter cells:").split()
for i in range(9):
    mat[i] = mat[i]

playboard = [["", "", ""],
             ["", "", ""],
             ["", "", ""]]

print("""
------------
| {} {} {} |
| {} {} {} |
| {} {} {} |
------------
""".format(mat[0], mat[1], mat[2],
           mat[3], mat[4], mat[5],
           mat[6], mat[7], mat[8]))

# horizontal X
if mat[0:2] and mat[0] != "" and mat[0] == "X":
    print("X Wins")
elif mat[3] == mat[4] and mat[4] == mat[5] and mat[3] != "" and mat[3] == "X":
    print("Game Wins")
elif mat[6] == mat[7] and mat[7] == mat[8] and mat[6] != "" and mat[6] == "X":
    print("Game Wins")
# horizontal 0
elif mat[0:2] and mat[0] != "" and mat[0] == "0":
    print("0 Wins")
elif mat[3] == mat[4] and mat[4] == mat[5] and mat[3] != "" and mat[3] == "0":
    print("0 Wins")
elif mat[6] == mat[7] and mat[7] == mat[8] and mat[6] != "" and mat[6] == "0":
    print("0 Wins")
# vertical X
elif mat[0] == mat[3] and mat[3] == mat[6] and mat[0] != "" and mat[0] == "X":
    print("X Wins")
elif mat[1] == mat[4] and mat[4] == mat[7] and mat[1] != "" and mat[1] == "X":
    print("X Wins")
elif mat[2] == mat[5] and mat[5] == mat[8] and mat[2] != "" and mat[2] == "X":
    print("X Wins")
# verical 0
elif mat[0] == mat[3] and mat[3] == mat[6] and mat[0] != "" and mat[0] == "0":
    print("0 Wins")
elif mat[1] == mat[4] and mat[4] == mat[7] and mat[1] != "" and mat[1] == "0":
    print("0 Wins")
elif mat[2] == mat[5] and mat[5] == mat[8] and mat[2] != "" and mat[2] == "0":
    print("0 Wins")
# diagonal
elif mat[0] == mat[4] and mat[4] == mat[8] and mat[0] != "" and mat[0] == "X":
    print("X Wins")
elif mat[2] == mat[4] and mat[4] == mat[6] and mat[2] != "" and mat[2] == "X":
    print("X Wins")
# diagonal 0
elif mat[0] == mat[4] and mat[4] == mat[8] and mat[0] != "" and mat[0] == "0":
    print("0 Wins")
elif mat[2] == mat[4] and mat[4] == mat[6] and mat[2] != "" and mat[2] == "0":
    print("0 Wins")
elif mat[0:9] != "":
    print("Game Draw")
