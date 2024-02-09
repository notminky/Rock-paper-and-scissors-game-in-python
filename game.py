import random
def get_choices():
    while True:
        my_choice=input("pick: rock, paper, scissores" "\n"+ "you choose: ").lower()
        options = ["rock","paper","scissores"]
        if my_choice in options:
            break
        else:
            print("try again")
    computer_choice = random.choice(options)
    choices= {"player":my_choice,"computer":computer_choice}
    return choices
def check_win(player,computer):
    print(f"Player chose {player}, Computer chose {computer}")
    if player==computer:
        return "it's a tie"
    elif player== "rock":
        if computer == "scissores":
            return "you win"
        else:
            return "you lose"
    elif player== "paper":
        if computer == "rock":
            return "you win"
        else:
            return "you lose"
    elif player== "scissores":
        if computer == "paper":
            return "you win"
        else:
            return "you lose"
while True:
    choices = get_choices()
    win = check_win(choices["player"], choices["computer"])
    print(win)
    play_again=input("do you wanna play again? (y,n)").lower()
    if play_again!= "y":
        break
