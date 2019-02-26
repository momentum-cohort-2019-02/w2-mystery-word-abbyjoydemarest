import string
import random


def add_file(filename):
   """Given a file, make a list out of it."""
   with open(filename) as file:
        text = file.read()
    # create a list of all the words
        all_words = text.split("\n")
   return all_words

def create_list_for_level(all_words):
   """ Given a list of words, create a new list for each level by selecting the words that fit within the required word length for that level."""
   easy_words = []
   normal_words = []
   hard_words = []
   for word in all_words:
      if len(word) >= 4 and len(word) <= 6:
         easy_words.append(word.casefold())
      if len(word) >= 6 and len(word) <= 8:
         normal_words.append(word.casefold())
      if len(word) >= 8:
         hard_words.append(word.casefold())
   return [easy_words, normal_words, hard_words]

def select_mystery_word(word_lists, user_choice):
   easy_words = word_lists[0]
   normal_words = word_lists[1]
   hard_words = word_lists[2]
   #user_choice = get_user_level_choice(user_choice)
   if user_choice == 'easy':
      mystery_word = random.choice(easy_words)
   if user_choice == 'normal':
      mystery_word = random.choice(normal_words)
   if user_choice == 'hard':
      mystery_word = random.choice(hard_words)
   #print(mystery_word)
   return mystery_word

def is_guess_a_letter(user_guess): 
   """ Given the user's input of 'guess' see if that guess meets the
   requirements that is a letter of length 1 and if it is in guess.isalpha"""
   # set requirements for the guess to meet to be a letter. Must be one in length and also in .isalpha
   return len(user_guess) == 1 and user_guess.isalpha()

def get_letter_guess_from_user():
   """Given the user's input of 'guess' continue to ask them for a guess until the guess is a letter in the English alphabet"""
    # ask for the guess, and lower case it.
   user_guess = input("""Guess a letter that you think is in the mystery word: """).casefold()
    # if the requirements for a guess are not met then ask them for a guess again __until__ the requirements are met.
    # Since it is until we will do a while loop, so while it does not meet the requirements that were predetermined.
   while not is_guess_a_letter(user_guess):
        # tell them it does not meet the requirement of being a letter
        print("Oh yikes! That was not a letter, silly!.")
        # ask them for another guess
        user_guess = input(
            "Guess a letter that you think is in the mystery word: ").casefold()
    # once we have received a guess that meets the requirements return the guess
   return user_guess

#this just needs to show the word
def get_word_to_display(word, letters_to_show,):
    """Given a word and guesses show the user "what the word looks like with correct guesses filled in and incorrect guesses left blank as "_". """
    #create a list for the displayed word to go into
    #breakpoint()
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
   #breakpoint()
   for letter in mystery_word.lower():
      if letter not in letters_guessed:
         #print("This is not finished.")
         return False
   return True

def game_is_over(mystery_word, letters_guessed, attempts):
   return determine_if_mystery_word_guessed(mystery_word, letters_guessed) or attempts == 0

def play_game():
   """ask the player if they would like to play again, if they do then start the game again, if they dont then end the game"""
   user_play_response = input("Would you like to play? yes or no: ")
   if user_play_response == 'yes':
      print("""Great... you are going down this time!
      ... Well, after I figure out how to get that while loop set up. 
      For now, you can run the program again :)
      good luck!!""")
   if user_play_response == 'no':
      return "Thank you have a nice life!"


if __name__ == "__main__":
   print("""
   Hello! We are going to play a game. \nYou are going to try to figure out the mystery word that I have chosen. \nFirst, pleaese select from the following modes: \n     'Easy' = words 4 to 6 letters in length \n     'Normal' = words 6 to 8 letters in length \n     'Hard' = words 8+ letters in length
   """)
   user_choice = None
   while user_choice not in ['easy', 'normal', 'hard']:
      user_choice = input("Type the name of your choice of modes: 'easy' , 'normal', or 'hard': ")
      print(f"You chose {user_choice} mode. Let us begin. May the odds be ever in your favor.")
   
   all_words = add_file('words.txt')
   word_lists = create_list_for_level(all_words)
   mystery_word = select_mystery_word(word_lists, user_choice)
   
   letters_guessed = []
   attempts = 8
   while not game_is_over(mystery_word, letters_guessed, attempts):
      print(get_word_to_display(mystery_word, letters_guessed))
      letter_guessed = get_letter_guess_from_user()
      if letter_guessed in letters_guessed:
         print("Nice try, but you already guessed that letter.")
      elif letter_guessed in mystery_word:
         print("Wooo! You are so smart! You guessed a correct letter!!")
         letters_guessed.append(letter_guessed)
      else:
         letters_guessed.append(letter_guessed)
         attempts -= 1
         print(f"Aw Shucks, that wasn't right. \n That is okay, you still have {attempts} attempts left.")

   if determine_if_mystery_word_guessed(mystery_word,letters_guessed):
      print(get_word_to_display(mystery_word, letters_guessed))
      print(f"Great news... You are a genius!! \n You  won!!! The word was {mystery_word.upper()}")
   else: 
      print(f"Sad day... You did not win. \n The word was {mystery_word.upper()}. \n Better Luck next time!")
   play_game()