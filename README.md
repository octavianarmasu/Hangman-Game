#Copyright Armasu Octavian

# Hangman Game in Python

This is a simple Hangman game implemented in Python, where you'll be guessing words in the Romanian language. The game offers three difficulty levels: easy, medium, and hard. The difficulty level determines the complexity of the words you'll be guessing.

## Instructions

1. **Clone the Repository**
   - Clone this repository to your local machine using the following command:

     ```bash
     git clone https://github.com/octavianarmasu/Hangman-Game
     ```

2. **Navigate to the Directory**
   - Change your current directory to the project folder:

     ```bash
     cd Hangman-Game
     ```

3. **Run the Game**
   - Execute the game by running the following command:

     ```bash
     python hangman.py
     ```

4. **Choose Difficulty**
   - At the beginning of the game, you will be prompted to choose a difficulty level: easy, medium, or hard. The difficulty level affects the complexity of the words you'll need to guess.

5. **Guessing Words**
   - The game will provide you with a series of underscores representing the letters in the word you need to guess. You will have a limited number of attempts to guess the word.
   - Enter one letter at a time. If the letter is in the word, it will be revealed; if not, you'll lose one of your attempts.
   - Keep guessing until you've guessed all the letters or run out of attempts.

6. **Win or Lose**
   - If you guess all the letters before running out of attempts, you win the game.
   - If you run out of attempts before guessing the word, you lose.
