import random

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
                   
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(logo)

READ = "r"
file_name = "C:/Users/DeAlwis_Consulting/OneDrive/Family/Yenula/python_work/Project/tkinterThings/scripts/dictionary.txt"
with open(file_name, READ, encoding="utf-8") as f_obj:
    lines = f_obj.readlines()
    lines = [i for i in lines if len(i) > 4]
    word = random.choice(lines)

stage = 1
find_word = ""
count = 0
num_letters = 1
underscore_letters = ("_ "*(len(word)-1)).strip()
while count != 6:
    if num_letters == len(word):
        print("Well done, you won! :)")
        break
        
    print(underscore_letters, "\n")
    guess_letter = input("Guess a letter: ").strip().lower()
    if guess_letter not in word:
        stage += 1
        count += 1
        print(underscore_letters)
        print(f"\nYou guessed {guess_letter}, that's not in the word. You lose a life. :(")
        print(stages[-stage])
    
    else:
        num_letters += 1
        
        index_in_word = [i*2 for i in range(len(word)) if word[i] == guess_letter]
        underscore_letters = list(underscore_letters)
            
        for i in index_in_word:
            del underscore_letters[i]
            underscore_letters.insert(i, guess_letter)
            
        underscore_letters = "".join(underscore_letters)
        print()
        print(underscore_letters, end="\n\n")
        print(stages[-stage])
        
print(f"The word was: {word}")
print("The computer is laughing because you lost. ;D")