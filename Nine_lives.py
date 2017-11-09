import random

lives = 10

words = ['berry', 'chokes', 'whores', 'honey', 'tiles', 'berta', 'sluts', 'harry'
        , 'boner', 'shored', 'short', 'bondage', 'cottage', 'pussy' ,'fussy']
secret_word = random.choice(words)
clue = []
index = 0
while index < len(secret_word):
    clue.append('?')
    index = index + 1
heart_symbol = u'\u2764'
guessed_word = False
unknown_letters = len(secret_word)

def update_clue(guessed_letter, secret_word, clue, unknown_letters):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
            unknown_letters = unknown_letters - 1
        index = index + 1

        return unknown_letters

difficulty = input('Choose level of difficulty (1, 2, 3)')
difficulty = int(difficulty)

if difficulty == 1:
    lives = 12
elif difficulty == 2:
    lives = 9
else:
    lives = 6    

while lives > 0:
    print(clue)
    print('Lives left: ' + heart_symbol * lives)
    guess = input('Guess a letter or the whole word: ')

    if guess == secret_word:
        guessed_word = True
        break
        

    if guess in secret_word:
        unknown_letters = update_clue(guess, secret_word, clue, unknown_letters)
    else:
        print('Incorrect, You lose a life')
        lives = lives - 1

    if unknown_letters == 0:
        guessed_word = True
        break
    
    
    

if guessed_word:
    print('You won! The secret word was ' + secret_word)

else:
    print('You lost! The secret word was ' + secret_word)
 
