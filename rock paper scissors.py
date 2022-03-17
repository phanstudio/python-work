import random

def main():
    gameContinue = True
    while gameContinue:
        score = 0
        game = True
        won = False
        while game:
            try:
                twoPlayers = input("Two players Yes[Y] or No[N]")
                if twoPlayers[0].lower() == "y" or twoPlayers[0].lower() == "n":
                    numberOfGames = int(input("Select the number of games: "))
                    if numberOfGames > 0:
                        game = False
                    else:
                        print("Choose a number above 0")
                else:
                    print("Choose btw yes or no")
            except:
                print("Select a valid number")
        for i in range(numberOfGames):
            userInput = False
            while not userInput:
                userHand = input("Pick Rock[R], Paper[P] or Scissors[S]: ")
                hand = userHand[0].lower()
                if hand == "r":
                    userInput = True
                    print("You picked Rock")
                elif hand == "p":
                    userInput = True
                    print("You picked Paper")
                elif hand == "s":
                    userInput = True
                    print("You picked Scissors")
                else:
                    print("Write the right operation")
            if twoPlayers[0].lower() == "n":
                for _ in range(3):
                    print(".", end= "")
                print()
            secondInput = False
            while not secondInput:
                if twoPlayers[0].lower() == "n":
                    botHand = random.randint(1, 3)
                else:
                    botHand = input("Pick Rock[R], Paper[P] or Scissors[S]: ")
                if botHand == 1 or botHand == "r":
                    secondInput = True
                    botHand = "r"
                    print("Cpu picked rock")
                elif botHand == 2 or botHand == "p":
                    secondInput = True
                    botHand = "p"
                    print("Cpu picked paper")
                elif botHand == 3 or botHand == "s":
                    secondInput = True
                    botHand = "s"
                    print("Cpu picked scissors")
                else:
                    print("Write the right operation")
            if botHand == hand:
                print("You tie")
                score += 0.5
            elif (botHand == "r" and hand == "s") or (botHand == "p" and hand == "r") or (botHand == "s" and hand == "p"):
                print("You Lost.")
            elif (botHand == "s" and hand == "r") or (botHand == "r" and hand == "p") or (botHand == "p" and hand == "s"):
                print("You Win!")
                score += 1
                won = True
        if won == True:
            if score > 1:
                print("You won " + str(score) + " games")
            else:
                print("You won " + str(score) + " game")
        else:
            print("You won 0 games")
        print("You scored " + str(round((score / numberOfGames) * 100)) + "%")
        if ((score / numberOfGames) * 100) > 50:
            print("You Won the game!")
        elif ((score / numberOfGames) * 100) < 50:
            print("You Lost the game.")
        else:
            print("You Tied")
        userYN = input("Do you want to continue the game Yes[Y] or No[N]? ")
        if userYN[0].lower() != "y" and userYN[:1].lower() != " y":
            gameContinue = False
            print("Thanks for playing")
            break
        else:
            print("Lets keep going")
            continue
    pass

main()
