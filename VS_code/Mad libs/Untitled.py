from random import shuffle
from getpass import getpass

def main():
    ques = []
    word = []
    player = []
    try:
        len_player = int(input("Enter number of players here:"))
    except Exception as e:
        print(e)
        main()


    for i in range(1,len_player+1):
        name = input("Enter player name here:")
        player.append(name)
    print(f"The order of the game is{player}")

    for i in range(0,len_player):
        word_in  = getpass(f"{player[i]} ,Enter a word")
        word.append(word_in)
    for i in range(0,len_player):
        ques_in  = getpass(f"{player[i]} ,Enter a question")
        ques.append(ques_in)
    for i in range(0,len_player):
        print(f"Question:{ques[i]} \n Response:{word[i]}")


main()
