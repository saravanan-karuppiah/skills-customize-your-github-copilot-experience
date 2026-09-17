
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a text-based Hangman game in Python by practicing string manipulation, loops, conditionals, user input, and random selection. Start with the provided `starter-code.py` file and complete the missing game logic.

## 📝 Tasks

### 🛠️ Set Up the Game State

#### Description

Complete the setup section in `starter-code.py` so each game selects a secret word and tracks the player's progress.

#### Requirements

Completed program should:

- Select a secret word randomly from the predefined `words` list.
- Initialize a collection for the letters the player has guessed.
- Set a maximum number of incorrect guesses and track the remaining attempts.
- Display the hidden word as underscores before the first guess.

### 🛠️ Implement the Guessing Loop

#### Description

Implement the main game loop so the player can guess letters until the word is revealed or no incorrect guesses remain.

#### Requirements

Completed program should:

- Ask the player for a letter and update the guessed letters after each turn.
- Reveal correctly guessed letters while keeping other letters hidden.
- Decrease the remaining attempts when the player guesses an incorrect letter.
- End when the player guesses every letter in the secret word or runs out of attempts.
- Print a clear win or lose message. For a loss, reveal the secret word.

For example, a game may display progress like this:

```text
Word: _ _ _ _ _ _
Guess a letter: p
Word: p _ _ _ _ _
```
