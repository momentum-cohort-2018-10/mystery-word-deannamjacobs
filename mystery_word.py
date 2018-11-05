import random

# print(repr(word_file.readlines()))


def clean_text(user_text):
    new_text = ""
    for char in user_text:
        if char.isalpha():
            new_text = new_text + char

    return new_text


easy_mode_words = []
normal_mode_words = []
hard_mode_words = []

with open('words.txt') as word_file:

    for all_words in word_file.readlines():

        if len(all_words) > 3 and len(all_words) < 7:
            easy_mode_words.append(clean_text(all_words))

        if len(all_words) > 5 and len(all_words) < 9:
            normal_mode_words.append(clean_text(all_words))

        if len(all_words) > 8:
            hard_mode_words.append(clean_text(all_words))

print(easy_mode_words)
print(normal_mode_words)
print(hard_mode_words)

user_text = input(
    "Please choose your level of difficulty.\
    Enter 1 for Easy Mode, 2 for Normal Mode, and 3 for Hard Mode.")

if user_text == "1":
    random.choice(easy_mode_words)
    word_to_guess = random.choice(easy_mode_words)
    print(word_to_guess)

if user_text == "2":
    random.choice(normal_mode_words)
    word_to_guess = random.choice(normal_mode_words)
    print(word_to_guess)

if user_text == "3":
    random.choice(hard_mode_words)
    word_to_guess = random.choice(hard_mode_words)
    print(word_to_guess)

# word_to_guess = ""
# print(len(word_to_guess))

user_text = (input(f"There are {len(word_to_guess)} letters in your word."))


def print_instructions():
    print("Guess the mystery word. You have 8 guesses to get it right.  Correct guesses don't
          count against the 8 guesses.  Good luck!")


letter_blanks = '_ ' * len(word_to_guess)
print(letter_blanks)

# display_word(word, letters)


def play_game():
    print_instructions()
    letter_to_guess = (letters in word_to_guess)
    letters_guessed = False
    guesses = 0


while not letters_guessed and guesses < 9:
    letter_from_user = input("What's your guess?: ")
    guesses += 1
    if letter_from_user == letter_to_guess:
        print("You got it right!")
        letters_guessed = True
    elif letter_from_user not in 'abcdefghijklmnopqrstuvwxyz':
        print("Your guess must be a letter!")
    else len(letter_from_user) != 1:
        print("You may guess only one letter at a time.")
