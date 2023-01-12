# Hangman (or Guess The Word)
### Description:
Created a single-file hangman game based on a verbal description of a homework assignment in a different intermediate Python programming class.
This version of hangman doesn't include a 'hanging man', so it could be called Guess The Word.

### Instructions:
If you wish to play, follow the below steps:
1. Open Command Prompt, and run 'python' or 'python3'. This should return the version of Python you are running and makes sure you have Python installed. If you do not have Python installed, there's plenty of guides on how to do so.

2. Download main.py and words.txt, and store them on the same directory (this could be your downloads folder, desktop, or any other folder, just as long as both files are in the same spot) This makes sure the Python script will be able to find and load from the text file of words.

3. Open main.py and run it!

### How it works:
The script (main.py) reads the text file (words.txt), a list of 800+ words, and randomly selects 1 word that the player will attempt to guess. Players will then select how many 'lives', or times they can get something wrong, they get. Users can then input letters or phrases consisting of the English alphabet and the program will respond differently based on whether the user inputs 1 character or multiple.

If a user provides a single character guess, the program will search the word to determine if the character is within it. If the character is within the word, the character will show up on the character slot of the word (an underscore), e. g. a user guessing 'f' for the word 'fun', the program will change its display from '_ _ _' to 'f _ _'. The program, which also displays a list of characters the user has not guessed, will replace the character with an underscore, e. g. 'A B C D E F G' becomes 'A B C D E _ G'. If the user provides an incorrect single character, the program will deduct a life.

If the user provides a multi-character guess, the program shifts from comparing characters to comparing the whole string, checking if that multi-line string is equivalent to the word itself, e. g. for input 'fu' if 'fu' equals 'fun'. If the multi-character input is not equivalent to the selected word, the program will deduct a life and compare the unique characters in the guess to the unique characters in the selected word. It'll then tell the user how many unique characters in the user's input match the unique characters in the selected word, but will not tell the user which characters these are. 

(This was implemented to counter some easy shortcuts such as guessing 'abcdefghijklmnopqrstuvwxyz')
