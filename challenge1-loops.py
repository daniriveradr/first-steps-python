'''Guess a number between 1 and 5: 3
Guess a number between 1 and 5: 4
You guessed it in 2 tries!
I tried several times to make it work but I couldn't get him to repeat the loop to request the number again
'''

import random 

guess_number = random.randint(1, 5)
print(f'Guess number: {guess_number}.')

your_number = int(input("Guess a number between 1 and 5: "))

count = 0

while guess_number != your_number:
  count = count + 1
  print(f'It took {count} rolls to roll a 5!')
else:
  print("Guess a number between 1 and 5: ")
