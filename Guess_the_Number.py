#GUESS THE NUMBER GAME
#Maximum chances are 5, hidden number is in Range 1-100
import random
hidden = random.randint(1, 100)
guesses = 5
while(guesses>0):
    ip = int(input("Enter a num to guess the hidden number in Range (1-100)\n"))
    if ip > hidden :
            guesses = guesses - 1
            print("guess is greater, Remaining guess chances : ",guesses)
            continue
    elif ip < hidden :
            guesses = guesses - 1
            print("guess is lower, Remaining guess chances : ", guesses)
            continue
    else:
            guesses = guesses - 1
            print("YOU WON, You have guessed the correct number in ",5-guesses," guesses")
            break
print("GAME OVER","\nHidden Number was ",hidden)