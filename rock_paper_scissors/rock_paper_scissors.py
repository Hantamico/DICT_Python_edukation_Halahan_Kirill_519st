import random


while True:
    choose = input("choose one of option: \n -Rock \n -Paper \n -Scissors \n -------------------\n>")
    combo_list = ["Rock", "Paper", "Scissors"]
    bot_choise = random.choice(combo_list)
    print(bot_choise)
    if bot_choise == "Rock" and choose == "Scissors":
        print("LOSE - Sorry, but the computer chose Rock")
    if bot_choise == "Rock" and choose == "Rock":
        print("DRAW - There is a draw Rock")
    if bot_choise == "Rock" and choose == "Paper":
        print("WIN - Well done. The computer chose Rock and failed")
    if bot_choise == "Paper" and choose == "Scissors":
        print("WIN - Well done. The computer chose Paper and failed")
    if bot_choise == "Paper" and choose == "Paper":
        print("DRAW - There is a draw Paper")
    if bot_choise == "Paper" and choose == "Rock":
        print("LOSE - Sorry, but the computer chose Paper")
    if bot_choise == "Scissors" and choose == "Scissors":
        print("DRAW - There is a draw Scissors")
    if bot_choise == "Scissors" and choose == "Rock":
        print("WIN - Well done. The computer chose Scissors and failed")
    if bot_choise == "Scissors" and choose == "Paper":
        print("LOSE - Sorry, but the computer chose Scissors")

