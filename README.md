# Hangman Game

This is a Python-based implementation of the classic **Hangman** game. In this game, the player has to guess a word one letter at a time. The player can make up to 6 incorrect guesses before the game ends. The game features simple ASCII art for the hangman figure that visualizes the player's progress.

## Features

- The game selects a random word from a predefined list.
- The user is prompted to guess one letter at a time.
- The incorrect guesses are visualized using an ASCII art hangman.
- The user can play the game multiple times by choosing to play again after each round.
- The game limits the number of incorrect guesses to 6.

# Example Game Play
Welcome to Hangman Game

Enter your name: John
Hello John I wish you best of luck!
The game is going to start!! Let's play!!

This is the Hangman Word: _ _ _ _ _ 
Enter your guess: e

   _____
  |     |
  |     |
  |     O
  |      
  |      
  |      
__|__

Wrong guess. 5 guesses remaining

This is the Hangman Word: _ _ _ _ _ 
Enter your guess: a

This is the Hangman Word: a _ _ _ a
Enter your guess: r

Congrats! You have guessed the word correctly!
Do you want to play again? y = yes, n = no
