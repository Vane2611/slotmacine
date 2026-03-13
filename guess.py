import random

number_to_guess = random.randint(1,100)
while True:
    try:
        guess = int(input('Guess a number betweeen 1 and 100: '))
        if guess < number_to_guess:
            print('That\'s lower')
        elif guess > number_to_guess:
            print('That\'s higher')
        else:
            print('Hurray you got it!!')
            break
    except ValueError:
        print('Please enter an integer.')