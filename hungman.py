import random
import time

#Initial Steps to invite users into the game:

print("\nWelcome to Hangman Game\n")
name = input("Enter your name: ")
print("Hello "+ name + " I wish you best of luck!")
time.sleep(2)
print("The game is going to start!!\nLets play!!")
time.sleep(3)


#The parameters we need to execute the game:
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = [
        "january", "border", "image","film","promise","kids","lungs","doll","rhyme","damage"
                   ,"plants", "ant"
    ]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_'*length
    already_guessed = []
    play_game = ""

#Loop to re-execute the game when the first round is finished:

def play_loop():
    global play_game
    play_game = input("Do you want to play again? y = yes, n = no\n")
    while play_game not in ["y", "n", "Y","N","Yes", "No"]:
        play_game = input("Do you want to play again? y = yes, n = no\n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks for playing our game >< We expect you back again!")
        exit()

#Initializing all the conditions required for the game:

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 6
    guess = input("This is the Hungman Word: "+ display + "Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     o \n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     O \n"
                 "  |     |\\\n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     O \n"
                  "  |    /|\\\n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     O \n"
                  "  |    /|\\\n"
                  "  |      \\\n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 6:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     O \n"
                  "  |    /|\\\n"
                  "  |    / \\\n"
                  "  |     \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_guessed,word)
            play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()


main()


hangman()