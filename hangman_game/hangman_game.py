import random
from collections import Counter

someWords = "apple banana mango strawberry " \
            "orange grape pineapple apricot lemon coconut watermelon " \
            "cherry papaya berry peach lychee muskmelon".split(' ')
word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')
    for i in word:
        #For printing the empty spaces for letters of the word
        print('_', end=' ')
    print()
    playing = True
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    try:
        while (chances > 0):
            print()
            chances -= 1
            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter')
                continue

            #Validation of the guess
            if not guess.isalpha():
                print('Enter letter only')
                continue
            elif len(guess) > 1:
                print('Enter single letter only')
                continue
            elif guess in letterGuessed:
                print('you have already guessed that letter')
                continue

            if guess in word:
                letterGuessed += guess

            for char in word:
                if char in letterGuessed:
                    print(char, end=' ')
                    correct += 1
                else:
                    print('_', end=' ')

            #if user has guessed all the letters
            if (Counter(letterGuessed) == Counter(word)):
                print()
                print("You've done!")
                break
        if chances == 0:
            print()
            print("You lose")
            print("The word was {}".format(word))
    except KeyboardInterrupt:
        print()
        print('Bye, try again')
        exit()


