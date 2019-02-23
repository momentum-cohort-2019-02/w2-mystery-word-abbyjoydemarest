import string
import random

def add_file():
   with open("words.txt") as file:
      text = file.read()  
   #create a list of all the words
      all_words = text.split("\n")
   return all_words

def create_list_for_level(all_words):
   easy_words = []
   normal_words = []
   hard_words = []
   for word in all_words:
      if len(word) >= 4 and len(word) <= 6:
         easy_words.append(word)
      elif len(word) >= 6 and len(word) <= 8:
         normal_words.append(word)
      elif len(word) >= 8:
         hard_words.append(word)
   return [easy_words, normal_words, hard_words]

#get the user to input their level choice
def get_user_level_choice():
   print("Hello! We are going to play a game. \nYou are going to try to figure out the mystery word that I have chosen. \nFirst, pleaese select from the following modes: \n     'Easy' = words 4 to 6 letters in length \n     'Normal' = words 6 to 8 letters in length \n     'Hard' = words 8+ letters in length")
   user_choice = input("Type the name of your choice of modes: ")
   #check to see if what they gave us and determine if it is 'Easy' 'Normal' or 'Hard
   while True:
      if user_choice == 'easy' or user_choice == 'normal' or user_choice == 'hard':
         return user_choice

#select the random word from the list correlating to that level
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
   return mystery_word
#select a random word from the list and make that the mystery_word

#show them the length of their mystery word.

#check to see if the guess is a letter
def check_if_guess_is_letter(mystery_word):
   """Given the guess, see if it is a letter. If it is a letter return the letter, if is it not a letter ask them the question again """
   mystery_word = ['c', 'a', 't',]
   #guesses = []
   correct_guess = []
   while correct_guess < mystery_word:
      guess = input("Please guess a letter that you think might be in this word: ")
      valid_letter = string.ascii_letters
      if guess in (valid_letter and mystery_word):
         correct_guess.append(guess)
         print("That letter is in the mystery word!")
      else:
         print("That letter is not in the mystery word")

         
   
   









#attempts = 0
#guesses = []
#correct_guess = []
#display_word = [mystery_word]
#for letter in guess:
 #  if letter == guess:
#      attempts += 1
#      guesses.append(guess)
#for letter in mystery_word:
  # if letter == guess:
  #    correct_guess.append(letter)
#print(correct_guess)
#print(attempts)



#get file to do random word
   # with open(words.txt) as file:
    #text = file.readliine()



if __name__ == "__main__":
   mystery_word = select_mystery_word(create_list_for_level(add_file()))
   check_if_guess_is_letter(mystery_word)
