from random import randrange as rr


def display_word_char(base_word: str, guessed_word: list, guess_: str):
    """Changes the visuals of the guessed word (underscores), deducts lives, and handles guessing for
    all inputs of a single character"""
    if guess_ not in base_word:
        # deducts a life from the user if their guess is not a letter in the word
        global lives
        lives -= 1
        print('Remaining Lives:', lives, '(-1)')
    elif guess_ in guessed_word:
        # if the user guesses a letter they've guessed before, this tells them that and does not deduct a life
        print('Please provide a letter(or letters) you have not already guessed!\nYour lives remain unchanged.')
        print('Remaining Lives:', lives)
    else:
        # if the user guesses a letter in the word, as long as that letter is in the word the program will loop through
        # and add that letter to the underscores (guessed_word) where it should go and remove it from the base word so
        # that when all occurrences of that letter are gone, the loop will end
        base_word = list(base_word)
        while guess_ in base_word:  # 'fills in' the letter on its spot(s) on the underscores and removes it from the
            # word being checked in the while loop (so it terminates)
            for i in range(len(base_word)):
                if base_word[i] == guess_:
                    base_word[i] = '_'
                    guessed_word[i] = guess_
        print('Remaining Lives:', lives)

    return ''.join(guessed_word)  # returns the guessed word joined together in string format


def display_word_chars(base_word: str, guessed_word: list, guess_: str):
    """Changes the visuals of the guessed word (underscores), deducts lives, and handles guessing for
        all inputs of multiple characters"""
    global lives  # func can now edit the global var lives

    if guess_ == base_word:  # checks for if the user gets the whole word right first try
        print('Remaining Lives:', lives)
        return guess_

    else:  # handles if the user gave a multi-char response that was not the selected word
        total_chars = len(set(guess_))
        correct_chars = 0
        for i in list(set(guess_)):
            if i in base_word:
                correct_chars += 1
        print(f'Sorry, that was not the correct word. \n'
              f'Out of the {total_chars} unique letters in that word, {correct_chars} were correct.')

        if correct_chars == len(set(base_word)):
            print('Even though your guess contains every unique letter in the word, you went just a bit overboard.')
        lives -= 1
        print('Remaining Lives:', lives, '(-1)')

        return ''.join(guessed_word)


def display_choices(letters_: str, guess_: str):
    """Modifies the display telling the user which letters they have not guessed"""
    letters_ = list(letters_)
    if guess_ == word or len(
            guess) > 1:  # handles if the user guesses the entire word correctly or gives any other multi-char response
        return ''.join(letters_)

    for g in guess_:
        if g.upper() in letters_:
            letters_[letters_.index(guess.upper())] = '_'
    return ''.join(letters_)


if __name__ == '__main__':
    print('=' * 100)
    print('Welcome to Hangman! This version does actually have a hanging man!'
          '\nYou get 7 lives, each one corresponds to a body part the hanged man can lose.'
          '\nIf you lose every part of the hanged man, you lose the game. ')
    print('For each guess you can only guess english letters, both capital and lowercase.\n'
          '\nIf you guess more than 1 letter in the guess, the program will assume you are'
          '\ntrying to guess the whole word and only fill in letters if you get the word correct.'
          '\nIf you do not get the word correct, the program will deduct 1 life and tell you how'
          '\nmany (but not which) unique letters you got correct in your guess.'
          '\n\nGood luck and have fun!\n')
    print('=' * 100)
    input('[Press ENTER to begin]')
    # just a whole lot of instructions and info for the user

    with open('words.txt') as words:
        wordlist = [word for word in
                    words.read().split()]  # creates a list of words to pull a word from using the text file 'words.txt'

    word = wordlist[rr(len(wordlist))].lower()
    # randomly generates an index based on the amt of words in the txt file and uses it to select a word
    guess_word = list('_' * len(word))
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lives = 7
    hanged_man = (
        # indices are the number of lives left (0-7)
        '_______\n ||    |\n ||\n ||\n ||\n ||\n_||_______',  # no limbs left
        '_______\n ||    |\n ||    O\n ||\n ||\n ||\n_||_______',  # only head left
        '_______\n ||    |\n ||    O\n ||    |\n ||\n ||\n_||_______',  # head and upper torso left
        '_______\n ||    |\n ||    O\n ||   /|\n ||\n ||\n_||_______',  # head, upper torso, 1 arm left
        '_______\n ||    |\n ||    O\n ||   /|\\\n ||\n ||\n_||_______',  # head, upper torso, both arms left
        '_______\n ||    |\n ||    O\n ||   /|\\\n ||    |\n ||\n_||_______',  # head, full torso, both arms left
        '_______\n ||    |\n ||    O\n ||   /|\\\n ||    |\n ||   /\n_||_______',  # head, full torso, both arms, 1 leg
        '_______\n ||    |\n ||    O\n ||   /|\\\n ||    |\n ||   / \\\n_||_______'  # unharmed
    )

    # print(word)  # UNCOMMENT THIS FOR TESTING PURPOSES

    while '_' in guess_word:
        if lives < 1:  # handling for when the user runs out of lives
            print('You lost! The word was:', word)
            break

        print('=' * 50, '\n', hanged_man[lives], ' ' * 10, 'Word:', ''.join(guess_word), '\n' + '=' * 50)
        guess = input('Guess a letter: ').lower().replace(' ', '', -1)
        while len(guess) < 1 or not guess.isalpha():  # handles invalid guesses
            guess = input('Please provide a letter (or letters) for a guess.\nTake your guess: ')
        if len(guess) > 1:
            guess_word = list(display_word_chars(word, guess_word, guess))  # uses func for handling multi-char inputs
        else:
            guess_word = list(display_word_char(word, guess_word, guess))  # uses func for handling single-char inputs

        letters = display_choices(letters, guess)
        print("Remaining Not Guessed Letters:", ' '.join(list(letters)))

    if lives > 0:
        print('=' * 50, '\n', hanged_man[lives], ' ' * 10, 'Word:', ''.join(guess_word), '\n' + '=' * 50)
        print('Congratulations! You won!')

input('[Press ENTER to quit]')  # added for anyone running in console where Exit Code 0 closes the application
