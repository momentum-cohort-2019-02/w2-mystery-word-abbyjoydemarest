import string
import random


def add_file():
    with open("words.txt") as file:
        text = file.read()
    # create a list of all the words
        all_words = text.split("\n")
    return all_words


def create_list_for_level(all_words):
    easy_words = []
    normal_words = []
    hard_words = []
    for word in all_words:
        if len(word) >= 4 and len(word) <= 6:
            easy_words.append(word.casefold())
        elif len(word) >= 6 and len(word) <= 8:
            normal_words.append(word.casefold())
        elif len(word) >= 8:
            hard_words.append(word.casefold())
    return [easy_words, normal_words, hard_words]

# get the user to input their level choice


def get_user_level_choice():
    choice = True
    while choice:
        print("Hello! We are going to play a game. \nYou are going to try to figure out the mystery word that I have chosen. \nFirst, pleaese select from the following modes: \n     'Easy' = words 4 to 6 letters in length \n     'Normal' = words 6 to 8 letters in length \n     'Hard' = words 8+ letters in length")
        user_choice = input(
            "Type the name of your choice of modes: 'easy' , 'normal', or 'hard': ")
        # check to see if what they gave us and determine if it is 'Easy' 'Normal' or 'Hard
        # valid_letter = string.ascii_letters
        # levels = ['easy', 'normal', 'hard',]
        # choice = True
        # while choice:
        if user_choice == 'easy':
            return user_choice
        elif user_choice == 'normal':
            return user_choice
        elif user_choice == 'hard':
            print("yess!!")
            return user_choice
        else:
            print("noo!!")


def select_mystery_word(word_lists):
    easy_words = word_lists[0]
    normal_words = word_lists[1]
    hard_words = word_lists[2]
    user_choice = get_user_level_choice()
    if user_choice == 'easy':
        mystery_word = random.choice(easy_words)
    elif user_choice == 'normal':
        mystery_word = random.choice(normal_words)
    elif user_choice == 'hard':
        mystery_word = random.choice(hard_words)
    print(mystery_word)
    return mystery_word


def is_guess_a_letter(user_guess):
    """ Given the user's input of 'guess' see if that guess meets the
    requirements that is a letter of length 1 and if it is in guess.isalpha"""
    # set requirements for the guess to meet to be a letter. Must be one in length and also in .isalpha
    return len(user_guess) == 1 and user_guess.isalpha()


def get_letter_guess_from_user():
    """Given the user's input of 'guess' continue to ask them for a guess until the guess is a letter in the English alphabet"""
    # ask for the guess, and lower case it.
    user_guess = input(
        "Guess a letter in the English alphabet that you think is in the mystery word: ").casefold()
    # if the requirements for a guess are not met then ask them for a guess again __until__ the requirements are met.
    # Since it is until we will do a while loop, so while it does not meet the requirements that were predetermined.
    while not is_guess_a_letter(user_guess):
        # tell them it does not meet the requirement of being a letter
        print("That was not a letter.")
        # ask them for another guess
        user_guess = input(
            "Guess a letter in the English alphabet that you think is in the mystery word: ").casefold()
    # once we have received a guess that meets the requirements return the guess
    return user_guess

#this just needs to be show the word
def get_word_to_display(word, letters_to_show,):
    """Given a word and guesses show the user "what the word looks like with correct guesses filled in and incorrect guesses left blank as "_". """
    #create a list for the displayed word to go into
    output_characters = []
    #create a for loop 
    for letter in word.lower():
        if letter in letters_to_show:
            output_characters.append(letter.upper())
        else:
            output_characters.append("_")
    return " ".join(output_characters)


def determine_if_mystery_word_guessed(mystery_word, letters_guessed):
   """Given the mystery word and the letters guessed correctly return true if all letters in the mystery word have been guessed. """
   for letter in mystery_word:
      if letter not in letters_guessed:
         print("This is not finished.")
         return False
   return True

def get_letters_guessed(user_guess, mystery_word):
   letters_guessed = []
   attempts = 8
   if user_guess in letters_guessed:
      print("You have already guessed that letter.")
   elif user_guess in mystery_word:
      print("You guessed a correct letter.")
      letters_guessed.append(user_guess)
   else:
      letters_guessed.append(user_guess)
      attempts -= 1
      print(f"""Sad day :( That letter was not in the mystery word.
               You have {attempts} attempts left. """)
   return letters_guessed

def game_is_over(mystery_word, letters_guessed, attempts):
   return determine_if_mystery_word_guessed(mystery_word, letters_guessed) or attempts == 0

if __name__ == "__main__":
 

   mystery_word = select_mystery_word(create_list_for_level(add_file()))
   user_guess = get_letter_guess_from_user()
   letters_guessed = get_letters_guessed(user_guess, mystery_word)
   attempts = 8

 
   while not game_is_over(mystery_word, letters_guessed, attempts):
      print(get_word_to_display(mystery_word, letters_guessed))
      letters_guessed = get_letters_guessed(user_guess, mystery_word)
      if determine_if_mystery_word_guessed(mystery_word, letters_guessed):
         print(f"Great news... You  won!!! The word was {get_letters_guessed(user_guess, mystery_word)}")
      else: 
         print(f"Sad day... You did not win. The word was {get_letters_guessed(user_guess, mystery_word)}")

