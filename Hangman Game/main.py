#imports
import random
from ASCII import HANGMANPICS
from word_list import WORD_LIST, easy_words, medium_words, hard_words

difficulty = int(input("What type of difficulty do you want(1 for easy, 2 for medium, 3 for hard and 4 if your feeling lucky): "))
chosen_word = ""
if difficulty == 1:
    chosen_word = random.choice(easy_words)
elif difficulty == 2:
    chosen_word == random.choice(medium_words)
elif difficulty == 3:
    chosen_word == random.choice(hard_words)
elif difficulty == 4:
    chosen_word == random.choice(WORD_LIST)
else:
    print("Please enter a correct number")
    exit()

placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"
print(placeholder) #blank conversion
print(chosen_word)

player_lives = 0

game_running = True
guessed_letters = []

while game_running: 
    word = ""   
    guess = input("Enter your letter: ").lower()
    for letter in chosen_word:
        if letter in guessed_letters:
            word += letter
        elif letter == guess:
            word += guess
            guessed_letters.append(guess)
        else:
            word += "_"
            
    if guess not in guessed_letters:
        player_lives += 1
        if player_lives == 6:
            game_running = False
            print("YUO LOOSE!")
            print(f"THE CORRECT ANSWER WAS {chosen_word.upper()}!!!!")

    print(word)
    print(HANGMANPICS[player_lives])

    if word == chosen_word:
        game_running = False
        print("YUO WIN!")
        print(f"THE CORRECT ANSWER IS {chosen_word.upper()}!!!")
    else:
        pass