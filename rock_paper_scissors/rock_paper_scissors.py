import random


def game():
    while True:
        choose = input("choose one of option: \n -Rock \n -Paper \n -Scissors \n -------------------\n>")
        combo_list = ["Rock", "Paper", "Scissors"]
        if choose in combo_list:
            bot_choice = random.choice(combo_list)
            print(bot_choice)
            if bot_choice == "Rock" and choose == "Scissors":
                print("LOSE - Sorry, but the computer chose Rock")
            if bot_choice == "Rock" and choose == "Rock":
                print("DRAW - There is a draw Rock")
            if bot_choice == "Rock" and choose == "Paper":
                print("WIN - Well done. The computer chose Rock and failed")
            if bot_choice == "Paper" and choose == "Scissors":
                print("WIN - Well done. The computer chose Paper and failed")
            if bot_choice == "Paper" and choose == "Paper":
                print("DRAW - There is a draw Paper")
            if bot_choice == "Paper" and choose == "Rock":
                print("LOSE - Sorry, but the computer chose Paper")
            if bot_choice == "Scissors" and choose == "Scissors":
                print("DRAW - There is a draw Scissors")
            if bot_choice == "Scissors" and choose == "Rock":
                print("WIN - Well done. The computer chose Scissors and failed")
            if bot_choice == "Scissors" and choose == "Paper":
                print("LOSE - Sorry, but the computer chose Scissors")
        elif choose == "exit":
            print("Bye!")
        else:
            print("Invalid input")
            exit()

game()
