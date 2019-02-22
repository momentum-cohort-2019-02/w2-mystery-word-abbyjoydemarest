import string
import random



with open("words.txt") as file:
  text = file.read()  
#create a list of all the words
all_words = text.split("\n")

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

#get the user to input their level choice
print("Hello! We are going to play a game. You are going to try to figure out the mystery word that I have chosen. First, pleaese select from the following modes: ")
#range for length of word = 4 to 6
print(("'Easy' = words 4 to 6 letters in length") +
#range for length of word = 6 to 8
("'Normal' = words 6 to 8 letters in length") +
#range for length of word = 8 +
("'Hard' = words 8+ letters in length"))
#ask for the length they want as an integer. 
user_choice = input("Type the name of your choice of modes: ")

#check to see if what they gave us and determine if it is 'Easy' 'Normal' or 'Hard
level_choice = True
while level_choice:
   if user_choice == 'easy' or user_choice == 'normal' or user_choice == 'hard':
      level_choice = False
   else:
      user_choice = input("Type the name of your choice of modes: ")

#select the random word from the list correlating to that level
for choice in user_choice:
   if user_choice == 'easy':
      mystery_word = random.choice(easy_words)
   elif user_choice == 'normal':
     mystery_word = random.choice(normal_words)
   elif user_choice == 'hard':
      mystery_word = random.choice(normal_words)
#select a random word from the list and make that the mystery_word
print(mystery_word)
#show them the length of their mystery word.


#def determine_if_guess_is_letter(letter, guess):
  # guess= print(input("Please guess a letter that you think might be in this word: "))
    #valid_letter = string.ascii_letters
    #for letter in guess:
       # if letter in valid_letter:
          #  return letter
       # else:
           # return determine_if_guess_is_letter


#get file to do random lword
   # with open(words.txt) as file:
    #text = file.readliine()



#if __name__ == "__main__":

