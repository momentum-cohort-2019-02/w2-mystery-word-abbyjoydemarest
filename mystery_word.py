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
   choice = True
   while choice:
      print("Hello! We are going to play a game. \nYou are going to try to figure out the mystery word that I have chosen. \nFirst, pleaese select from the following modes: \n     'Easy' = words 4 to 6 letters in length \n     'Normal' = words 6 to 8 letters in length \n     'Hard' = words 8+ letters in length")
      user_choice = input("Type the name of your choice of modes: 'easy' , 'normal', or 'hard': ")
      #check to see if what they gave us and determine if it is 'Easy' 'Normal' or 'Hard
      #valid_letter = string.ascii_letters
      #levels = ['easy', 'normal', 'hard',]
      #choice = True
      #while choice:
      if user_choice == 'easy': 
         return user_choice
      elif user_choice == 'normal':
         return user_choice
      elif user_choice == 'hard':
         print("yess!!")
         return user_choice
      else:
         print("noo!!")



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
   #([mystery_word])
#select a random word from the list and make that the mystery_word

#show them the length of their mystery word.

#check to see if the guess is a letter
def check_if_guess_is_letter(mystery_word):
   """Given the guess, see if it is a letter. If it is a letter return the letter, if is it not a letter ask them the question again """
   mystery_word = mystery_word.casefold
   mystery_word = list(mystery_word)
   display_word = []
   guesses = []
   correct_guess = []
   attempts = 0
   for letter in mystery_word:
      if letter not in guesses:
         display_word.append("_")
      if letter in guesses:
         letter
   print(str(mystery_word)) 
   #[letter if letter in guess else "_" for letter in mystery_word]
   while correct_guess < display_word:
      guess = input("Please guess a letter that you think might be in this word: ")
      #breakpoint()
      guesses.append(guess)
      valid_letter = string.ascii_letters
      if guess in valid_letter :
         guesses.append(guess)
         attempts += 1
         print(mystery_word)
         #print(correct_guess)
         print("That is a letter!")
         print(f"You have had {attempts} attempts.")
         if guess in mystery_word:
            correct_guess.append(guess)
            print("that letter is in the mystery word")
         else:
            print("that letter is not in the mystery word")
            continue
      else:
         #print(guesses)
         print("That is not a letter")
         continue
   return print(f"you solved it!! The mystery word was {str(mystery_word)}")




         
   
   









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
