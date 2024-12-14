import random
def guessingGame():
    lives = 1
    numberToGuess = random.randint(1,10)
    while lives == 1:
        guessedNumber = input("Guess number between 1 and 10.")
        if guessedNumber == numberToGuess:
            print("You have sucsessfully won! Did you know that 99.99% of gamblers give up right after they are about to hit a winning streak?")
        else:
            print("You were so close! Don't quit now! Did you know that 99.99% of gamblers quit right before they hit it big?")
            print ("The number was " + str(numberToGuess) + ". You should play again!")
            lives = lives - 1
        gambleCore()
def rps():
    playerChoice = input("Do you want to choose ROCK, PAPER, or SCISSORS? Press E to exit.")
    while playerChoice != "ROCK" or playerChoice != "PAPER" or playerChoice != "SCISSORS": 
        if playerChoice.upper() == "ROCK":
            print("You chose Rock!")
            print ("You have lost. The Computer has chosen PAPER.")
            break
        elif playerChoice.upper() == "SCISSORS":
            print("You chose SCISSORS!")
            print ("You have lost. The computer has chosen ROCK.")
            break
        elif playerChoice.upper() == "PAPER":
            print("You chose PAPER!")
            print ("You have lost. The computer has chosen SCISSORS")
            break
        elif playerChoice.upper() == "E":
            gamblrCore()
        else:
            print ("You have failed at the second most simple step. How do expect to play the game lke this?")
   
def bJack():
    cards = set()
    suits = ["spades", "hearts", "clubs", "diamonds"]
    royalty = ["K", "J", "Q", "A"]
    
    for i in range(2,9):
        for suit in suits:
            cards.add((str(i), suit))
    
        
    print(cards)
    
    
def gambleCore():
    print ( "Welcome to the mingame interface! You can play a guessing game, rock paper scissors, and Black Jack")
    minigamechoice = input("type 1  for Guess the Nummber, 2 for rock paper scisors, and press 3 for Black Jack.")
    while minigamechoice != str(1) or minigamechoice != str(2) or minigamechoice != str3:
        if minigamechoice == str(1):
            print ("You are playing the nunmber guessing game.")
            guessingGame()
        elif minigamechoice == str(2):
            print ("You are playing rock paper scissors.")
            rps()
        elif minigamechoice == str(3):
            print ("You are playing Black Jack.")
            bJack()
        else:
            print("You have failed at the most simple step. how can you expect to play the games like this?")
            minigamechoice = input("type 1  for Guess the nummber, 2 for rock paper scisors, and press 3 for Mad Libs.")
    
gambleCore()