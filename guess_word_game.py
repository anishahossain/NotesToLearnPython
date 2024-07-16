secret_word = 'love'
tries = 0
tries_limit = 3
print('hint: ai')
while tries < tries_limit:
    guess = input('Guess: ')
    tries += 1
    if guess.lower() == secret_word:
        print(tries)
        break
else:
    print('wrong word')





