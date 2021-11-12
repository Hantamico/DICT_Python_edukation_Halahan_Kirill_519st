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
