# Hangman
Play hangman in a fun simulation with over 200 words! Difficulties range from 4-6 letters to 13+ letters. Utilizes if statements, recursion, methods, and file-handling. Code inspired and partially sourced from KiteHQ

---

# Hangman.py
- Contains the main method
- Presents a choice menu to choose difficulty
- Randomly generates a number depending on the choice
- Pulls a word from the library file and hides it as ___
- Each correct guess reveals a letter, each incorrect guess takes a try
- After either running out of tries or guessing the word correctly, game ends
- Asks if you would like to keep playing then repeats

---

# wordlibrary.txt
- A comprehensive collection of all 200+ words used in the simulation
- Hangman.py opens this file and reads a random line depending on user difficulty preference
